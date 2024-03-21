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

def test_update_society_name():
    # Assuming society_id exists in the database
    update_data = {"id": 1, "name": "New Society Name"}

    # Send a POST request to update society name
    response = requests.post(f"{BASE_URL}/update_society_name", json=update_data)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Check the response message
    assert response.json() == {"message": "Name updated successfully"}

def test_update_event_with_empty_name_or_location():
    # Assuming event_id exists in the database
    event_id = 1
    update_data_name_empty = {"id": event_id, "name": ""}
    update_data_location_empty = {"id": event_id, "location": ""}

    # Send a POST request to update event name with an empty string
    response_name_empty = requests.post(f"{BASE_URL}/update_event_name", json=update_data_name_empty)

    # Check that the response status code is 200 (OK)
    assert response_name_empty.status_code == 200

    # Check the response message for name update
    assert response_name_empty.json() == {"message": "Invalid Name input"}

    # Send a POST request to update event location with an empty string
    response_location_empty = requests.post(f"{BASE_URL}/update_event_location", json=update_data_location_empty)

    # Check that the response status code is 200 (OK)
    assert response_location_empty.status_code == 200

    # Check the response message for location update
    assert response_location_empty.json() == {"message": "Invalid Location input"}

def test_update_event_location_and_time_not_empty():
    # Assuming event_id exists in the database
    event_id = 1
    update_data_location_not_empty = {"id": event_id, "location": "New Location"}
    update_data_time_not_empty = {"id": event_id, "datetime": "2024-12-01 11:00:00"}

    # Send a POST request to update event location with a non-empty string
    response_location_not_empty = requests.post(f"{BASE_URL}/update_event_location", json=update_data_location_not_empty)

    # Check that the response status code is 200 (OK)
    assert response_location_not_empty.status_code == 200

    # Check the response message for location update
    assert response_location_not_empty.json() == {"message": "Location updated successfully"}

    # Send a POST request to update event time with a non-empty string
    response_time_not_empty = requests.post(f"{BASE_URL}/update_event_time", json=update_data_time_not_empty)

    # Check that the response status code is 200 (OK)
    assert response_time_not_empty.status_code == 200

    # Check the response message for time update
    assert response_time_not_empty.json() == {"message": "DateTime updated successfully"}

def test_update_user_interests():
    # Assuming user_id exists in the database
    user_id = 1
    interests = [1, 2, 3]  # Assuming interest IDs exist in the database

    update_data = {"id": user_id, "interests": interests}

    # Send a POST request to update user interests
    response = requests.post(f"{BASE_URL}/update_user_interests", json=update_data)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Check the response message
    assert response.json() == {"message": "Interests updated successfully"}

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
