from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user,login_manager,UserMixin,LoginManager,login_required,logout_user
from werkzeug.security import generate_password_hash,check_password_hash
from flask import flash



local_server=True
app = Flask(__name__)
app.secret_key="bhkghehedbhdv%$@%@&^#&(5455)"



# dbconnections
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/databasename'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/ecommerceguvi'
db=SQLAlchemy(app)


# Initialise the tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))

class Signup(UserMixin,db.Model):
    userid=db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String(50))
    lastname=db.Column(db.String(50))
    email=db.Column(db.String(80))
    password=db.Column(db.String(1000))
    phone=db.Column(db.Integer)

@app.route("/") #http://127.0.0.1:5000/
def home():
    return render_template("index.html")

@app.route("/login",methods=['GET','POST']) 
def login():
    if request.method=="POST":
        print("form has submitted")


    return render_template("login.html")


@app.route("/signup",methods=['GET','POST']) 
def signup():
    if request.method=="POST":
        firstname=request.form.get("fname")
        lastname=request.form.get("lname")
        email=request.form.get("email")
        mobilenumber=request.form.get("mobilenum")
        password=request.form.get("pass1")
        confirmpassword=request.form.get("pass2")
        if password!=confirmpassword:
            flash("Password is not matching","primary")
            return render_template("signup.html")
        genpass=generate_password_hash(password)
        # print(firstname,lastname,email,mobilenumber,genpass,confirmpassword)
        query=Signup(firstname=firstname,lastname=lastname,email=email,password=genpass,phone=mobilenumber)
        db.session.add(query)
        db.session.commit()
        return "User is added"


  

    return render_template("signup.html")

@app.route("/test")
def test():
    try:
        query=Test.query.all()
        print(query)
        return f"Database is connected"
    except Exception as e:
        return f"Database is not connected {e}"




app.run(debug=True)