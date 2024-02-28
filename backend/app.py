from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'deliverable3_testing_db'
 
mysql = MySQL(app)

@app.route('/')
def index():
  return 'Server Works!'

@app.route('/greet')
def say_hello():
  return 'Hello world'

@app.route('/test')
def test():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM userSocieties')
    data = cur.fetchall()
    cur.close()
    return str(data)

@app.route('/uinterests')                       #its /uinterests?user_id=...  
def return_userinterests():
    user_id = request.args.get('user_id')       #need to change to request.form.get when real
    if not user_id:
       return "no user id"
    
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM userInterests WHERE user_id = %s', (user_id,))
    data = cur.fetchall()
    cur.close()
    return str(data)

@app.route('/set_uinterest', methods=['GET', 'POST'])     #its /set_uinterest?user_id=...&interest=....&scale=...
def set_userinterest():
    user_id = request.args.get('user_id')          #need to change to form
    interest = request.args.get('interest')
    scale = request.args.get('scale')
    
    if not user_id:
       return "missing user id"
    if not interest:
       return "missing interest"
    if not scale:
       return "missing scale"
    
    cur = mysql.connection.cursor()
    #original value (just for testing)
    cur.execute('SELECT scale FROM userInterests WHERE user_id = %s AND interest = %s;', (user_id, interest))
    old_scale = cur.fetchone()
    #update
    cur.execute('UPDATE userInterests SET scale = %s WHERE user_id = %s AND interest = %s;', (scale, user_id, interest))
    mysql.connection.commit()  # commit changes
    cur.close()
  
    return f"Interest changed for user {user_id}: {interest} {old_scale[0]} -> {scale}"

if __name__ == '__main__':
    app.run(debug=True)