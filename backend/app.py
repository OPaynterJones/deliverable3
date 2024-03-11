from flask import Flask, jsonify, request, make_response
from flask_mysqldb import MySQL, MySQLdb
from flask_cors import CORS
import bcrypt
import uuid
from algorithm import train


app = Flask(__name__)


CORS(app, supports_credentials=True)


app.config["MYSQL_HOST"] = "db"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "deliverable3_testing_db"

mysql = MySQL(app)

@app.route('/ping', methods=['GET'])
def ping():
    try:
        # Try to connect to the database
        conn = mysql.connection
        cur = conn.cursor()

        # If the connection is successful, close it and return a success message
        cur.close()
        return jsonify({"message": "Database connection successful"}), 200
    except Exception as e:
        # If the connection fails, return an error message
        return jsonify({"message": f"Database connection failed: {str(e)}"}), 500

@app.route('/train')
def train_algorithm():
    return train()

@app.route("/uinterests")  # its /uinterests?user_id=...
def return_userinterests():
    user_id = request.args.get(
        "user_id"
    )  # need to change to request.form.get when real
    if not user_id:
        return "no user id"

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM userInterests WHERE user_id = %s", (user_id,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


@app.route(
    "/set_uinterest", methods=["GET", "POST"]
)  # its /set_uinterest?user_id=...&interest=....&scale=...
def set_userinterest():
    user_id = request.args.get("user_id")  # need to change to form
    interest = request.args.get("interest")
    scale = request.args.get("scale")

    if not user_id:
        return "missing user id"
    if not interest:
        return "missing interest"
    if not scale:
        return "missing scale"

    cur = mysql.connection.cursor()
    # original value (just for testing)
    cur.execute(
        "SELECT scale FROM userInterests WHERE user_id = %s AND interest = %s;",
        (user_id, interest),
    )
    old_scale = cur.fetchone()
    # update
    cur.execute(
        "UPDATE userInterests SET scale = %s WHERE user_id = %s AND interest = %s;",
        (scale, user_id, interest),
    )
    mysql.connection.commit()  # commit changes
    cur.close()

    return f"Interest changed for user {user_id}: {interest} {old_scale[0]} -> {scale}"


@app.route("/login", methods=["POST"])
def login():
    cookie = request.cookies.get("session_token")
    app.logger.debug(f"Session token cookie: {cookie}")

    data = request.get_json()
    username = data["email"]
    password = data["password"].encode("utf-8")

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM users WHERE email = %s", (username,))
    user_dbrecord = cur.fetchone()

    if user_dbrecord:
        column_names = [column[0] for column in cur.description]
        user_dict = dict(zip(column_names, user_dbrecord))

        if username and bcrypt.checkpw(password, user_dict["password"].encode("utf-8")):
            cur.execute(
                "SELECT * FROM sessions WHERE user_id = %s", (user_dict["user_id"],)
            )
            existing_session = cur.fetchone()

            if existing_session:
                column_names = [column[0] for column in cur.description]
                session_token_dict = dict(zip(column_names, existing_session))
                session_token = session_token_dict["session_token"]
            else:
                session_token = str(uuid.uuid4())
                app.logger.debug(f"Type of session UUID: {type(session_token)}")
                cur.execute(
                    "INSERT INTO sessions (user_id, session_token) VALUES (%s, %s)",
                    (user_dict["user_id"], session_token),
                )
                mysql.connection.commit()

            cur.close()

            response = make_response({"message": "Login Successful"})
            response.set_cookie("session_token", session_token)
            return response, 200

    return jsonify({"message": "Invalid username or password"}), 401


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data["email"]
    password = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())
    cur = mysql.connection.cursor()
    try:
        cur.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s)",
            (email, password),
        )
        mysql.connection.commit()

        return jsonify({"message": "User registered successfully"}), 201
    except MySQLdb.IntegrityError as error:
        mysql.connection.rollback()
        return jsonify({"message": f"User registration unsuccessful {str(error)}"}), 500
    finally:
        cur.close()


@app.route("/check_session", methods=["GET"])
def check_session():
    app.logger.debug("Received session authentication request")
    session_token = request.cookies.get("session_token")

    if not session_token:
        return jsonify({"message": "No session token found"}), 401

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sessions WHERE session_token = %s", (session_token,))
    session_dbrecord = cur.fetchone()
    cur.close()

    if session_dbrecord:
        app.logger.debug("User is logged in")
        return jsonify({"message": "User is logged in"}), 200
    else:
        app.logger.debug("Invalid session token")
        return jsonify({"message": "Invalid session token"}), 401


if __name__ == "__main__":
    app.run(debug=True)
