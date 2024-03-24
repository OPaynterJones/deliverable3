import os
import requests
import pymysql
import uuid

# The base URL of your Flask app. You might need to adjust this depending on your setup.
BASE_URL = "http://localhost:5000"

# Database connection details. Replace with your actual details.
DB_HOST = "db"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "deliverable3_testing_db"


def get_db_connection():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)


def test_db_connection_endpoint():
    # Send a GET request to the /test_db_connection endpoint
    response = requests.get(f"{BASE_URL}/ping")

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Check the response data
    assert response.json() == {"message": "Database connection successful"}


def test_simple_db_query():
    # Connect to the database
    conn = get_db_connection()
    cur = conn.cursor()

    # Perform a simple query (replace with your actual query)
    cur.execute("SELECT * FROM users")

    # Fetch the result
    result = cur.fetchone()

    # Check that the result is not None (i.e., the query was successful)
    assert result is not None

    # Close the cursor and the connection
    cur.close()
    conn.close()


def test_register_new_user():
    # Test data
    email = f"test-{uuid.uuid4()}@example.com"
    data = {"email": email, "password": "test123"}

    # Send a POST request to the /register endpoint
    response = requests.post(f"{BASE_URL}/register", json=data)

    print(str(response))
    # Check that the response status code is 201 (Created)
    assert response.status_code == 201

    # Check the response data
    assert response.json() == {"message": "User registered successfully"}

    # Check the database
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s", (data["email"],))
    user = cur.fetchone()
    cur.close()
    conn.close()

    assert user is not None


def test_register_existing_user():
    # Test data
    email = f"test-{uuid.uuid4()}@example.com"
    data = {"email": email, "password": "test123"}

    # Send a POST request to the /register endpoint
    response = requests.post(f"{BASE_URL}/register", json=data)
    print(str(response))
    # Check that the response status code is 201 (Successful)
    assert response.status_code == 201

    # Send a POST request to the /register endpoint
    response = requests.post(f"{BASE_URL}/register", json=data)
    print(str(response))
    # Check that the response status code is 500 (Internal Server Error)
    assert response.status_code == 500

    # Check the response data
    assert "User registration unsuccessful" in response.json()["message"]

    # Check the database
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM users WHERE email = %s", (data["email"],))
    count = cur.fetchone()[0]
    cur.close()
    conn.close()

    assert count == 1


def test_login_and_session_authorization():
    # Generate a unique email address using a UUID
    email = f"test-{uuid.uuid4()}@example.com"

    # Test data
    register_data = {"email": email, "password": "test123"}

    # Send a POST request to the /register endpoint to register a new user
    register_response = requests.post(f"{BASE_URL}/register", json=register_data)
    print(str(register_response))
    # Check that the response status code is 201 (Created)
    assert register_response.status_code == 201

    # Check the response data
    assert register_response.json() == {"message": "User registered successfully"}

    # Now that the user is registered, we can proceed with the login test
    login_data = {"email": email, "password": "test123"}

    # Send a POST request to the /login endpoint
    login_response = requests.post(f"{BASE_URL}/login", json=login_data)

    # Check that the response status code is 200 (OK)
    assert login_response.status_code == 201

    # Check the response data
    assert login_response.json() == {"message": "Login Successful"}

    # Check that a session token was set
    assert "session_token" in login_response.cookies

    # Get the session token
    session_token = login_response.cookies.get("session_token")

    # Send a GET request to the /check_session endpoint with the session token
    check_session_response = requests.get(
        f"{BASE_URL}/check_session", cookies={"session_token": session_token}
    )

    # Check that the response status code is 200 (OK)
    assert check_session_response.status_code == 201

    # Check the response data
    assert check_session_response.json() == {"message": "User is logged in"}


def test_get_image():
    # Test image filename
    filename = "test-image.png"

    # Create a test image file
    with open(f"images/{filename}", "wb") as f:
        f.write(b"test image content")

    try:
        # Send a GET request to the /images/<filename> endpoint
        response = requests.get(f"{BASE_URL}/images/{filename}")

        # Check that the response status code is 200 (OK)
        assert response.status_code == 200

        # Check the response content
        assert response.content == b"test image content"
    finally:
        # Clean up: Delete the test image file
        os.remove(f"images/{filename}")


def test_get_random_event():

    # Send a GET request to the endpoint
    response = requests.get(f"{BASE_URL}/recommend_event")

    # Assert status code is 200 (success)
    assert response.status_code == 200

    # Parse JSON response
    data = response.json()
    print(response.content)
    # Assert data is a dictionary
    assert isinstance(data, dict)

    # Assert expected keys are present
    assert "id" in data
    assert "title" in data
    assert "description" in data
    assert "time" in data
    assert "image_url" in data
    assert "society_id" in data

def test_register_user_with_interests():
    # Test data
    email = f"test-{uuid.uuid4()}@example.com"
    data = {
        "email": email,
        "password": "test123",
        "interests": [{"interest": "Technology", "scale": 5}, {"interest": "Music", "scale": 3}]
    }

    # Send a POST request to the /register endpoint
    response = requests.post(f"{BASE_URL}/register", json=data)

    # Check that the response status code is 201 (Created)
    assert response.status_code == 201

    # Check the response data
    assert response.json() == {"message": "User registered successfully"}

    # Check the database for user registration and interests
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s", (data["email"],))
    user = cur.fetchone()
    cur.execute("SELECT * FROM userInterests WHERE user_id = %s", (user[0],))
    interests = cur.fetchall()
    cur.close()
    conn.close()

    assert user is not None
    assert len(interests) == 2  # Assuming two interests were added

def test_get_society_details():
    # Test data
    society_id = 1

    # Send a GET request to the /society_details/<society_id> endpoint
    response = requests.get(f"{BASE_URL}/society_details/{society_id}")

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Check the response data
    assert "name" in response.json()
    assert "description" in response.json()
    assert "image_url" in response.json()
    assert response.json()["society_id"] == society_id

def test_update_user_interests():
    # Test data
    email = "existing_user@example.com"
    new_interests = [{"interest": "Sports", "scale": 4}, {"interest": "Art", "scale": 5}]

    # Send a PUT request to the /update_interests endpoint
    response = requests.put(f"{BASE_URL}/update_interests/{email}", json=new_interests)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Check the response data
    assert response.json() == {"message": "Interests updated successfully"}

    # Check the database for updated interests
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    cur.execute("SELECT * FROM userInterests WHERE user_id = %s", (user[0],))
    interests = cur.fetchall()
    cur.close()
    conn.close()

    assert user is not None
    assert len(interests) == 2  # Assuming two interests were updated

def test_delete_event():
    # Test data
    event_id = 1

    # Send a DELETE request to the /events/<event_id> endpoint
    response = requests.delete(f"{BASE_URL}/events/{event_id}")

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Check the response data
    assert response.json() == {"message": "Event deleted successfully"}

    # Check the database to ensure the event is deleted
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM events WHERE event_id = %s", (event_id,))
    event = cur.fetchone()
    cur.close()
    conn.close()

    assert event is None

def test_edit_society_page_as_committee_member():
    # Test data
    user_email = "committee_member@example.com"
    society_id = 1

    # Send a GET request to the /edit_society_page endpoint
    response = requests.get(f"{BASE_URL}/edit_society_page/{society_id}", headers={"user_email": user_email})

    # Check that the response status code is 200 (OK) or 403 (Forbidden) depending on user's role
    assert response.status_code in [200, 403]

    if response.status_code == 200:
        # If the user is a committee member, they should be allowed to edit the page
        assert response.json() == {"message": "Edit society page"}
    else:
        # If the user is not a committee member, they should not be allowed to edit the page
        assert response.json() == {"message": "Unauthorized. User is not a committee member."}
