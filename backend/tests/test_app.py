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
