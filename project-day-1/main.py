from flask import Flask,render_template

app = Flask(__name__)

@app.route("/") #http://127.0.0.1:5000/
def home():
    return render_template("index.html")

@app.route("/login") #http://127.0.0.1:5000/login
def login():
    return "<h1>Login Page</h1>"


app.run(debug=True)