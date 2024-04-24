from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user,login_manager,UserMixin,LoginManager,login_required,logout_user
from werkzeug.security import generate_password_hash,check_password_hash
from flask import flash,redirect,url_for
from flask_login import current_user
from datetime import datetime
import os
from werkzeug.utils import secure_filename


local_server=True
app = Flask(__name__)
app.secret_key="bhkghehedbhdv%$@%@&^#&(5455)"



login_manager=LoginManager(app)
login_manager.login_view='login'

# configuration for handling images which is uploaded in database
app.config['UPLOAD_FOLDER']='static/uploads/'
app.config['ALLOWED_EXTENSIONS']={'png','jpg','jpeg','gif'}
app.config['MAX_CONTENT_LENGTH']= 16*1024*1024 #16mb



# dbconnections
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/databasename'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/ecommerceguvi'
db=SQLAlchemy(app)


@login_manager.user_loader
def load_user(userid):
    return Signup.query.get(userid)



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
    phone=db.Column(db.String(12))

    def get_id(self):
        return self.userid



class Products(db.Model):
    pid=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(50))
    productname=db.Column(db.String(100))
    price=db.Column(db.String(100))
    category=db.Column(db.String(100))
    description=db.Column(db.String(1000))
    stock=db.Column(db.String(100))
    pimage=db.Column(db.String(1000))
    timestamp=db.Column(db.String(1000))

@app.route("/") #http://127.0.0.1:5000/
def home():
    products=Products.query.all()
    return render_template("index.html",products=products)

@app.route("/login",methods=['GET','POST']) 
def login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("pass1")
        user=Signup.query.filter_by(email=email).first()
        if user and check_password_hash(user.password,password):
            login_user(user)
            flash("Login Success","success")
            return redirect(url_for('profile'))
        else:
            flash("Invalid Credentails","danger")
            return redirect(url_for('login'))
       


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
            return redirect(url_for("signup"))
        
        fetchemail=Signup.query.filter_by(email=email).first()
        fetchphone=Signup.query.filter_by(phone=mobilenumber).first()
        if fetchemail or fetchphone:
            flash("User Already Exists","warning")
            return redirect(url_for("signup")) 
        
        if len(mobilenumber)!=10:
            flash("Please Enter 10 digit Number","warning")
            return redirect(url_for("signup"))
        
        genpass=generate_password_hash(password)
        # print(firstname,lastname,email,mobilenumber,genpass,confirmpassword)

        # query=Signup(firstname=firstname,lastname=lastname,email=email,password=genpass,phone=mobilenumber)
        # db.session.add(query)
        # db.session.commit()

        query=f"INSERT INTO `signup` (`firstname`,`lastname`,`email`,`password`,`phone`) VALUES ('{firstname}','{lastname}','{email}','{genpass}','{mobilenumber}')"
        with db.engine.begin() as conn:
            conn.exec_driver_sql(query)
            flash("Signup Is Success Please Login","success")
            return redirect(url_for('login'))

    return render_template("signup.html")

@app.route("/test")
def test():
    try:
        query=Test.query.all()
        print(query)
        return f"Database is connected"
    except Exception as e:
        return f"Database is not connected {e}"

@app.route("/profile")
@login_required
def profile():
    userdata=Signup.query.filter_by(email=current_user.email).first()
    return render_template("profile.html",userdata=userdata)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout Success","primary")
    return redirect(url_for('login'))




@app.route('/addproduct',methods=['GET','POST'])
@login_required
def addproduct():
    if request.method=="POST":
        email=request.form['email']
        pname=request.form['pname']
        pprice=request.form['pprice']
        pcategory=request.form['pcategory']
        pdesc=request.form['pdes']
        pstock=request.form['pcount']
        pimage=request.files['pimage']
        date=datetime.now()
        if pimage:
            filename=secure_filename(pimage.filename)
            pimage.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            query=Products(email=email,productname=pname,price=pprice,category=pcategory,description=pdesc,stock=pstock,pimage=pimage.filename,timestamp=date)
            db.session.add(query)
            db.session.commit()
            flash("Product is uploaded","success")
            return redirect(url_for('addproduct'))

    return render_template("addproduct.html")


@app.route('/product/<int:id>', methods=['GET','POST'])
def productdetails(id):
    product=Products.query.filter_by(pid=id).first()
    return render_template('productdetail.html',product=product)

app.run(debug=True)