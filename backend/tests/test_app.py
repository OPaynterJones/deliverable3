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
    assert login_response.status_code == 200

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
    assert check_session_response.status_code == 200

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

def test_create_new_society_existing_name():
    # Test data: Existing society name
    existing_name = "ABACUS"
    society_data = {"name": existing_name, "description": "Description of the society"}

    # Send a POST request to the create society endpoint
    response = requests.post(f"{BASE_URL}/create_society", json=society_data)

    # Check that the response status code is 400 (Bad Request)
    assert response.status_code == 500

def test_get_user_society_role():
    # Test data: User ID and Society ID
    user_id = 1
    society_id = 1

    # Mock the request payload
    request_data = {"user_id": user_id, "society_id": society_id}

    # Send a GET request to the get_user_society_role endpoint
    response = requests.get(f"{BASE_URL}/get_user_society_role", json=request_data)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Parse JSON response
    data = response.json()

    # Assert response data is fetched correctly
    assert isinstance(data, list)


def test_get_user_societies():
    # Test data: User ID
    user_id = 1

    # Mock the request payload
    request_data = {"id": user_id}

    # Send a GET request to the get_user_societies endpoint
    response = requests.get(f"{BASE_URL}/get_user_societies", json=request_data)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Parse JSON response
    data = response.json()

    # Assert response data is fetched correctly
    assert isinstance(data, list)

    # Check that each entry contains a society_id
    for entry in data:
        assert "society_id" in entry

def test_update_event_location():
    # Test data: Event ID and new location
    event_id = 1
    new_location = "New Location"

    # Mock the request payload
    request_data = {"id": event_id, "location": new_location}

    # Send a POST request to the update_event_location endpoint
    response = requests.post(f"{BASE_URL}/update_event_location", json=request_data)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Check the response data
    assert response.json() == {"message": "Location updated successfully"}

    # Check that the location has been updated in the database
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        f"SELECT location FROM events WHERE event_id = {event_id}"
    )
    updated_location = cur.fetchone()[0]
    cur.close()
    conn.close()

    assert updated_location == new_location
