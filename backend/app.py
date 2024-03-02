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
@app.route("/user_data")
def get_user_data():
    user_id = request.args.get("id", default=-1, type=int)
    
    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

# get name from table users by user_id
@app.route("/get_user_name")
def get_user_name():
    data = request.json
    user_id = data.get("user_id")

    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT name FROM users WHERE user_id = {user_id}")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

# create new user set username, password, name to table users
@app.route("/create_user", methods=["POST"])
def set_user_data():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    data = request.json

    username = data.get("username")
    password = data.get("password")
    name     = data.get("name")

    cursor = mysql.connection.cursor()
    cursor.execute(f"INSERT INTO users (username, password, name) VALUES ({username}, {password}, {name})")
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': "User added successfully"})

# set updated password from table users by user_id
@app.route("/update_user_password")
def set_user_password():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    data = request.json

    user_id  = data.get("id")
    password = data.get("password")

    cursor = mysql.connection.cursor()
    cursor.execute(f"UPDATE users SET password = {password} WHERE user_id = {user_id})")
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': "Password updated successfully"})

# set updated name from table users by user_id
@app.route("/update_user_name")
def set_user_name():
    if not request.is_json:
        return jsonify({"message": "Content type not supported (Not json)"})
    data = request.json

    user_id = data.get("id", default=-1, type=int)
    name    = data.get("name", type=str)

    cursor = mysql.connection.cursor()
    cursor.execute(f"UPDATE users SET password = {name} WHERE user_id = {user_id})")
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': "Name updated successfully"})






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
