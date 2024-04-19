from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# dbconnections
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/databasename'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/ecommerceguvissss'
db=SQLAlchemy(app)


# Initialise the tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))

@app.route("/") #http://127.0.0.1:5000/
def home():
    return render_template("index.html")

@app.route("/login",methods=['GET','POST']) 
def login():
    if request.method=="POST":
        print("form has submitted")


    return render_template("login.html")


@app.route("/signup") 
def signup():
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