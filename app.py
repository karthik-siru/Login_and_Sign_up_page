
from flask import Flask , render_template , request 

app = Flask(__name__)

#configure database 

import psycopg2 as pg 

dbconn =  pg.connect ("dbname=user")
cursor =  dbconn.cursor()


@app.route('/')
def hello_world():
    cursor.execute("CREATE TABLE users (id serial PRIMARY KEY, username text not null , password text not null , email text not null );")
    return render_template("signup.html")

@app.route('/form_login', methods = ['GET','POST'])
def check_login():
    uname  = request.form['username']
    pswd   = request.form['password']
    
    try :
       cursor.execute("SELECT * FROM users;")
       l = cursor.fetchall()
       for i in l :
            if i[0] == uname and i[1] ==pswd :
                return render_template("welcome.html",info = uname)
            if i[0] == uname or i[1] ==pswd :
                return render_template("login.html", info = "wrong-details")
       return render_template("signup.html", info ="no user found")
    except :
        return render_template("signup.html", info ="no user found")



@app.route('/form_register' , methods = ['GET' ,'POST'])
def register_user():
    mail = request.form['mail']
    name = request.form['username']
    password =  request.form['password']
    
    try  :
        l = cursor.fetchall()

        for i in l :
            if i[0] == name :
                return render_template("signup.html", info = "username taken")
    except :

        cursor.execute("INSERT INTO users(username,password,email) VALUES (%s,%s,%s)",(name , password ,mail))
        dbconn.commit()

    return render_template("welcome.html", info = name )

@app.route('/login.html')
def login_page():
    return render_template("login.html")

@app.route('/signup.html')
def signup_page():
    return render_template("signup.html")

