from flask import Flask, render_template
from wtform_fields import *
from flask_sqlalchemy import SQLAlchemy

#configure app
app = Flask(__name__)
app.secret_key = 'replace later'

db = SQLAlchemy()

#configure database
DB_URL = 'postgresql+pg8000://yignpyyvaonkjd:fa5709c2b802c74b5d0973b2dfc345e2debd6c1ce08598beff2dfe0d21456911@ec2-18-209-187-54.compute-1.amazonaws.com:5432/d4lsqn1i5nvulf'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

class User(db.Model):
    __tablename__ =  "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique  = True, nullable = False)
    password = db.Column(db.String(), nullable = False)

@app.route("/")
def index():
    return render_template("index.html")
  
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/app")
def application():
    return render_template("application.html")

@app.route("/signup", methods=['GET','POST'])
def signup():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # check username exists/duplication
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            return "This username is already taken!"
        # Add new user to the database
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "New username has been successfully created!"
    return render_template("signup.html", form = reg_form)

@app.route("/login")
def login():
    return render_template("login.html")
  
@app.route("/terms")
def terms():
    return render_template("terms.html")

if __name__ == "__main__":
    app.run(debug=True)
    
db.init_app(app)