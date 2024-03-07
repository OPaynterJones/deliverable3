from flask import Flask, jsonify, request, json
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins=["http://localhost:3000"])

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
    cursor.execute(f"INSERT INTO users (username, password, name) VALUES ({username}, {password}, {name})")
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
    cursor.execute(f"UPDATE users SET password = {password} WHERE user_id = {user_id}")
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
    cursor.execute(f"UPDATE users SET password = {name} WHERE user_id = {user_id}")
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
@app.route("/create_society")
def set_society_data():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    name = request_data.get("name")

    cursor = mysql.connection.cursor()
    cursor.execute(f"INSERT INTO societies (name) VALUES ({name})")
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
    cursor.execute(f"UPDATE societies SET name = {name} WHERE society_id = {society_id}")
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

# create new event set society_id, name to table events
@app.route("/create_event", methods=["POST"])
def set_event_data():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    society_id = request_data.get("society_id")
    name       = request_data.get("name")

    cursor = mysql.connection.cursor()
    cursor.execute(f"INSERT INTO events (society_id, name) VALUES ({society_id}, {name})")
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

    cursor = mysql.connection.cursor()
    cursor.execute(f"UPDATE events SET name = {name} WHERE event_id = {event_id}")
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
    datetime = request_data.get("datetime") # in mySQL format YYYY-MM-DD HH:MI:SS

    cursor = mysql.connection.cursor()
    cursor.execute(f"UPDATE events SET datetime = {datetime} WHERE event_id = {event_id}")
    mysql.connection.commit()
    cursor.close()
    return json({"message": "DateTime updated successfully"})


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
@app.route("/update_user_interests")
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
# get user role by user_id and society_id
@app.route("/get_user_society_role", methods=["GET"])
def get_user_society_role():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    user_id    = request_data("user_id")
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

    user_id    = request_data("user_id")
    society_id = request_data.get("society_id")

    cursor = mysql.connection.cursor()
    cursor.execute(f"INSERT INTO userSocieties (society_id, user_id) VALUES ({user_id}, {society_id})")
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "User added to society successfully"})

# set user role by user_id and society_id
@app.route("/update_user_society_role", methods=["POST"])
def set_user_society_role():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    request_data = request.json

    user_id    = request_data("user_id")
    society_id = request_data.get("society_id")
    role       = request_data.get("role")

    cursor = mysql.connection.cursor()
    cursor.execute(f"UPDATE userSocieties SET role = {role} WHERE user_id = {user_id} AND society_id = {society_id}")
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
@app.route("/update_event_interests")
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




@app.route("/")
def index():
    return "Server Works!"

@app.route("/greet")
def say_hello():
    return "Hello world"

@app.route("/test")
def test():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM userSocieties")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route("/uinterests")  # its /uinterests?user_id=...
def return_userinterests():
    user_id = request.args.get("user_id")  # need to change to request.form.get when real
    if not user_id:
        return "no user id"

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM userInterests WHERE user_id = %s", (user_id,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


@app.route("/set_uinterest", methods=["GET", "POST"])  # its /set_uinterest?user_id=...&interest=....&scale=...
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


if __name__ == "__main__":
    app.run(debug=True)
