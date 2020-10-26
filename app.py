from flask import Flask
from flask import render_template, request, redirect
import sqlite3

app = Flask(__name__)

# MySql database configuration
conn = sqlite3.connect("test123.db",check_same_thread=False)
cur = conn.cursor()
#cur.execute("""CREATE TABLE users_details ( First_name text,Last_name text, Email text, Contact_number text, Password text) """)
#c.execute("INSERT INTO customers VALUES('John', 'Elder','john@codemy.com')")
#c.execute("INSERT INTO customers VALUES('Tim', 'Smith','tim@codemy.com')")
#c.execute("INSERT INTO customers VALUES('Mary', 'Brown','john@codemy.com')")

#many_customer = [('Wes','Brown','wes@brown.com'),('Steph','Kuewa','steph@kuewa.com'),('Dan','Pas','dan@pas.com'),]
#c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customer)
#print("Command executed succesfully...")


@app.route('/', methods=['GET', 'POST'])
def display_home_page():
    return render_template('home.html')


@app.route('/register', methods=['POST', 'GET'])
def insert_user_details():

    if request.method == 'POST':
        first_name = request.form['fname']
        last_name = request.form['lname']
        email = request.form['email']
        contact_number = request.form['cnumber']
        password = request.form['pwd']
        tup = (first_name,last_name,email,contact_number,password)

        if first_name and last_name and email and contact_number and password:

            cur.execute("INSERT INTO users_details VALUES (?,?,?,?,?)", tup)
            conn.commit()
        return render_template('login.html')
    else:
        return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pwd']
        if email and password:
            query = "SELECT First_name FROM users_details where Email=\""+email+"\" and Password=\""+password+"\""
            print(query)
            cur.execute(query)
            data = cur.fetchall()
            print(data)
            return render_template('user_profile.html',data=data)
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run()
