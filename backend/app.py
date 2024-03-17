import sys

import numpy as np
from flask import Flask, jsonify, request, make_response, send_from_directory
from flask_mysqldb import MySQL, MySQLdb
from flask_cors import CORS
from datetime import datetime
import bcrypt
import uuid
from algorithm import train, predict_interest


app = Flask(__name__)


CORS(app, supports_credentials=True)

app.config["MYSQL_HOST"] = "db"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "deliverable3_testing_db"

mysql = MySQL(app)

"""
# unserialise JSON object from a string (force flask to read string as JSON)
def handle_non_json():
    data = json.loads(request.data)
    return data
"""

# get all data from table users by user_id
@app.route("/user_data", methods=["GET"])
def get_user_data():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    user_id = request_data.get("id")
    
    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
    fetch_data = cursor.fetchall()
    cursor.close()
    return jsonify(fetch_data)


""" User Table """
# get name from table users by user_id
@app.route("/get_user_name", methods=["GET"])
def get_user_name():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    user_id = request_data.get("id")

    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT name FROM users WHERE user_id = {user_id}")
    fetch_data = cursor.fetchall()
    cursor.close()
    return jsonify(fetch_data)

# create new user set username, password, name to table users
@app.route("/create_user", methods=["POST"])
def set_user_data():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    username = request_data.get("username")
    password = request_data.get("password")
    name     = request_data.get("name")

    cursor = mysql.connection.cursor()
    cursor.execute(f"INSERT INTO users (username, password, name) VALUES ('{username}', '{password}', '{name}')")
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "User added successfully"})

# set updated user password by user_id
@app.route("/update_user_password", methods=["POST"])
def set_user_password():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    user_id  = request_data.get("id")
    password = request_data.get("password")

    cursor = mysql.connection.cursor()
    cursor.execute(f"UPDATE users SET password = '{password}' WHERE user_id = {user_id}")
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "Password updated successfully"})

# set updated user name by user_id
@app.route("/update_user_name", methods=["POST"])
def set_user_name():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    user_id = request_data.get("id")
    name    = request_data.get("name")

    cursor = mysql.connection.cursor()
    cursor.execute(f"UPDATE users SET name = '{name}' WHERE user_id = {user_id}")
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "Name updated successfully"})


""" Societies Table """
# get society name by society_id
@app.route("/get_society_name", methods=["GET"])
def get_society_name():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    society_id = request_data.get("id")

    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT name FROM societies WHERE society_id = {society_id}")
    fetch_data = cursor.fetchall()
    cursor.close()
    return jsonify(fetch_data)

# create new society set name to table societies
@app.route("/create_society", methods=["POST"])
def set_society_data():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    name = request_data.get("name")

    cursor = mysql.connection.cursor()
    cursor.execute(f"INSERT INTO societies (name) VALUES ('{name}')")
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "Society added successfully"})

# update society name by society_id
@app.route("/update_society_name", methods=["POST"])
def set_society_name():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    society_id = request_data.get("id")
    name       = request_data.get("name")

    cursor = mysql.connection.cursor()
    cursor.execute(f"UPDATE societies SET name = '{name}' WHERE society_id = {society_id}")
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "Name updated successfully"})


""" Events Table """
# get event name by event_id
@app.route("/get_event_name", methods=["GET"])
def get_event_name():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    event_id = request_data.get("id")

    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT name FROM events WHERE event_id = {event_id}")
    fetch_data = cursor.fetchall()
    cursor.close()
    return jsonify(fetch_data)

# get event data by event_id
@app.route("/get_event_data", methods=["GET"])
def get_event_data():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    event_id = request_data.get("id")

    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT * FROM events WHERE event_id = {event_id}")
    fetch_data = cursor.fetchall()
    cursor.close()
    return jsonify(fetch_data)

# get event by society_id
@app.route("/get_society_events", methods=["GET"])
def get_society_events():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    society_id = request_data.get("id")

    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT event_id, name FROM events WHERE society_id = {society_id}")
    fetch_data = cursor.fetchall()
    cursor.close()
    return jsonify(fetch_data)

# create new event set society_id, name, datetime, location to table events
@app.route("/create_event", methods=["POST"])
def set_event_data():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    society_id = request_data.get("society_id")
    name       = request_data.get("name")
    datetime   = request_data.get("datetime") # SQL DateTime format YYYY-MM-DD HH:MI:SS
    location   = request_data.get("location")

    if name is "" or name is None:
        name = "Default Social Name"

    #default_datetime = "{today} 23:59:59".format(today=date.today()) # default datetime = end of day
    default_datetime = "2024-12-01 10:00:00"
    # if no datetime given, must provide default value
    try:

        datetime.fromisoformat(datetime)
    except:
        datetime = default_datetime

    default_location = "The Plug & Tub"
    # if no location given, must provide default value
    if location is "" or location is None:
        location = default_location

    cursor = mysql.connection.cursor()
    cursor.execute(f"INSERT INTO events (society_id, name, datetime, location) VALUES ({society_id}, '{name}', '{datetime}', '{location}')")
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "Event added successfully"})

# update event name by event_id
@app.route("/update_event_name", methods=["POST"])
def set_event_name():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    event_id = request_data.get("id")
    name     = request_data.get("name")

    if name is "" or name is None:
        return jsonify({"message": "Invalid Name input"})

    cursor = mysql.connection.cursor()
    cursor.execute(f"UPDATE events SET name = '{name}' WHERE event_id = {event_id}")
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "Name updated successfully"})

# update event datetime by event_id
@app.route("/update_event_time", methods=["POST"])
def set_event_time():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    event_id = request_data.get("id")
    datetime = request_data.get("datetime") # SQL DateTime format YYYY-MM-DD HH:MI:SS

    try:
        datetime.fromisoformat(datetime)
    except:
        return jsonify({"message": "Invalid DateTime input"})

    cursor = mysql.connection.cursor()
    cursor.execute(f"UPDATE events SET datetime = '{datetime}' WHERE event_id = {event_id}")
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "DateTime updated successfully"})

# update event location by event_id
@app.route("/update_event_location", methods=["POST"])
def set_event_location():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    event_id = request_data.get("id")
    location = request_data.get("location")

    if location is "" or location is None:
        return jsonify({"message": "Invalid Location input"})

    cursor = mysql.connection.cursor()
    cursor.execute(f"UPDATE events SET location = '{location}' WHERE event_id = {event_id}")
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "Location updated successfully"})


""" Interests Table """
# get all interests
@app.route("/get_interests", methods=["GET"])
def get_interests():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT interest FROM interests")
    fetch_data = cursor.fetchall()
    cursor.close()
    return jsonify(fetch_data)


""" User interest Table """
# get user interest scores
@app.route("/get_user_interests", methods=["GET"])
def get_user_interests():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    user_id = request_data.get("id")

    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT interest, scale FROM userInterests WHERE user_id = {user_id}")
    fetch_data = cursor.fetchall()
    cursor.close()
    return jsonify(fetch_data)

# update user interest scores
@app.route("/update_user_interests", methods=["POST"])
def set_user_interests():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    user_id         = request_data.get("id")
    interest_scores = request_data.get("interest_scores") # json array of [[interest, scale]]

    """
    need to figure out how to break down the array of interest scores to update the db
    """


    return jsonify({"message": "Interests updated successfully"})


""" User societies Table """
# get societies user is a member of
@app.route("/get_user_societies", methods=["GET"])
def get_user_societies():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    user_id    = request_data.get("id")

    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT society_id FROM userSocieties WHERE user_id = {user_id}")
    fetch_data = cursor.fetchall()
    cursor.close()
    return jsonify(fetch_data)

# get user role by user_id and society_id
@app.route("/get_user_society_role", methods=["GET"])
def get_user_society_role():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    user_id    = request_data.get("user_id")
    society_id = request_data.get("society_id")

    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT role FROM userSocieties WHERE user_id = {user_id} AND society_id = {society_id}")
    fetch_data = cursor.fetchall()
    cursor.close()
    return jsonify(fetch_data)

# add user to society by user_id and society_id
@app.route("/add_user_society_member", methods=["POST"])
def set_user_society_member():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    user_id    = request_data.get("user_id")
    society_id = request_data.get("society_id")

    cursor = mysql.connection.cursor()
    cursor.execute(f"INSERT INTO userSocieties (society_id, user_id, role, join_date) VALUES ({society_id}, {user_id}, 'member', CURRENT_DATE)")
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "User added to society successfully"})

# set user role by user_id and society_id
@app.route("/update_user_society_role", methods=["POST"])
def set_user_society_role():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    user_id    = request_data.get("user_id")
    society_id = request_data.get("society_id")
    role       = request_data.get("role")

    cursor = mysql.connection.cursor()
    cursor.execute(f"UPDATE userSocieties SET role = '{role}' WHERE user_id = {user_id} AND society_id = {society_id}")
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "Role updated successfully"})


""" User events Table """
# get event by user_id and event_id
@app.route("/get_user_events", methods=["GET"])
def get_user_events():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    user_id = request_data.get("id")

    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT event_id FROM userEvents WHERE user_id = {user_id}")
    fetch_data = cursor.fetchall()
    cursor.close()
    return jsonify(fetch_data)

# add user to event by user_id and event_id
@app.route("/add_user_event_member", methods=["POST"])
def set_user_event_member():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    user_id  = request_data.get("user_id")
    event_id = request_data.get("event_id")

    cursor = mysql.connection.cursor()
    # !!!
    # WHY IS USER_EVENT PRIMARY_KEY = {user_id, event_id}!!! In userSocieties Primary_key = {society_id, user_id}
    # !!!
    cursor.execute(f"INSERT INTO userEvents (user_id, event_id) VALUES ({user_id}, {event_id})")
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "User added to event successfully"})


""" Events interest Table """
# get event interest scores
@app.route("/get_event_interests", methods=["GET"])
def get_event_interests():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    event_id = request_data.get("id")

    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT interest, scale FROM eventInterests WHERE event_id = {event_id}")
    fetch_data = cursor.fetchall()
    cursor.close()
    return jsonify(fetch_data)

# update event interest scores
@app.route("/update_event_interests", methods=["POST"])
def set_event_interests():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    event_id        = request_data.get("id")
    interest_scores = request_data.get("interest_scores") # json array of [[interest, scale]]

    """
    need to figure out how to break down the array of interest scores to update the db
    """


    return jsonify({"message": "Interests updated successfully"})


@app.route("/uinterests")  # its /uinterests?user_id=...
def return_userinterests():
    user_id = request.args.get("user_id")  # need to change to request.form.get when real
    if not user_id:
        return "no user id"

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM userInterests WHERE user_id = %s", (user_id,))
    
# @app.route(
#     "/set_uinterest", methods=["GET", "POST"]
# )  # its /set_uinterest?user_id=...&interest=....&scale=...
# def set_userinterest():
#     user_id = request.args.get("user_id")  # need to change to form
#     interest = request.args.get("interest")
#     scale = request.args.get("scale")

#     if not user_id:
#         return "missing user id"
#     if not interest:
#         return "missing interest"
#     if not scale:
#         return "missing scale"

#     cur = mysql.connection.cursor()
#     # original value (just for testing)
#     cur.execute(
#         "SELECT scale FROM userInterests WHERE user_id = %s AND interest = %s;",
#         (user_id, interest),
#     )
#     old_scale = cur.fetchone()
#     # update
#     cur.execute(
#         "UPDATE userInterests SET scale = %s WHERE user_id = %s AND interest = %s;",
#         (scale, user_id, interest),
#     )
#     mysql.connection.commit()  # commit changes
#     cur.close()

#     return f"Interest changed for user {user_id}: {interest} {old_scale[0]} -> {scale}"


@app.route("/ping", methods=["GET"])
def ping():
    try:
        # Try to connect to the database
        return jsonify({"message": "Database connection successful"}), 200
    except Exception as e:
        # If the connection fails, return an error message
        return jsonify({"message": f"Database connection failed: {str(e)}"}), 500


@app.route("/predict", methods=["GET"])
def predict():
    request_data = request.json
    user_id = request_data.get("user_id")

    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT scale FROM userInterests WHERE user_id = {user_id}")
    fetch_data = cursor.fetchall()
    cursor.close()

    interests_array = np.array([item[0] for item in fetch_data]).reshape(1, -1)
    predictions = predict_interest(interests_array)

    # Update predicted interests in interestPredictions table
    cursor = mysql.connection.cursor()
    for prediction in predictions:
        society_name, predicted_interest = prediction
        cursor.execute(
            f"UPDATE interestPredictions SET predicted_interest = {predicted_interest} WHERE name = '{society_name}' AND user_id = {user_id}"
        )
    mysql.connection.commit()
    cursor.close()

    return jsonify(predictions)


@app.route("/suggest_event", methods=["GET"])
def suggest_event():
    try:
        request_data = request.json
        user_id = request_data.get("user_id")
        if not user_id:
            return jsonify({"error": "user_id is required"}), 400

        cur = mysql.connection.cursor()
        today = datetime.now().date()

        cur.execute(
            "SELECT name FROM interestPredictions WHERE user_id = %s ORDER BY predicted_interest DESC",
            (user_id,),
        )
        predicted_societies = cur.fetchall()
        suggested_events = []

        for society in predicted_societies:
            society_name = society[0]

            # Query to get the upcoming event related to the predicted society
            cur.execute(
                """
                SELECT e.event_id, e.event_name, e.event_time
                FROM events e
                JOIN societies s ON e.society_id = s.society_id
                WHERE s.name = %s AND e.event_time >= %s
                ORDER BY e.event_time ASC
                LIMIT 1
            """,
                (society_name, today),
            )

            event = cur.fetchone()
            if event:
                # If an event is found, append it to the suggested_events list and break the loop
                suggested_events.append(
                    {
                        "event_id": event[0],
                        "event_name": event[1],
                        "event_time": event[2].strftime("%Y-%m-%d %H:%M:%S"),
                    }
                )
                break  # Exit the loop as soon as an event is found

        cur.close()

        if not suggested_events:
            return (
                jsonify({"error": "No events found for the top predicted societies"}),
                404,
            )

        return jsonify(suggested_events)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/tables")
def return_tables():
    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT * FROM interestPredictions WHERE user_id = 1 ORDER BY predicted_interest"
    )
    data = cur.fetchall()
    cur.close()

    return str(data)


@app.route("/uinterests")  # its /uinterests?user_id=...
def return_userinterests():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM interests")

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


@app.route("/recommend_event")
def get_recommended_event():
    try:
        conn = mysql.connection
        cur = conn.cursor()

        # Execute query to get random event
        query = "SELECT * FROM events ORDER BY RAND() LIMIT 1;"
        cur.execute(query)
        event = cur.fetchone()

        # Check if event is found
        if event:
            app.logger.debug(event[5])
            # Prepare data with image path
            event_data = {
                "id": event[0],
                "title": event[1],
                "description": event[2],
                "location": event[3],
                "time": event[4],
                "image_url": event[5],  # Construct image URL
                "society_id": event[6],
            }
            return jsonify(event_data), 200
        else:
            return jsonify({"message": "No events found"}), 404

    except Exception as e:
        return jsonify({"message": f"Error fetching events: {str(e)}"}), 500


@app.route("/societies/<society_name>")
def get_society_details(society_name):
    app.logger.debug(society_name)
    try:
        cur = mysql.connection.cursor()

        cur.execute("SELECT * FROM societies WHERE name = %s", (society_name,))
        society_data = cur.fetchone()

        if society_data:
            society_details = {
                column[0]: value for column, value in zip(cur.description, society_data)
            }
            return jsonify(society_details), 200
        else:
            return jsonify({"message": f"Society '{society_name}' not found"}), 404

    except Exception as e:
        return jsonify({"message": f"Error fetching society details: {str(e)}"}), 500


@app.route("/images/<filename>")
def get_image(filename):
    try:
        return send_from_directory("images", filename)
    except FileNotFoundError:
        return jsonify({"message": "Image not found"}), 404

    except Exception as e:
        return jsonify({"message": "An error occurred"}), 500


if __name__ == "__main__":
    train()
    app.run(debug=True)
