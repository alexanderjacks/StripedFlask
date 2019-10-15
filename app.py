from flask import Flask, session, redirect, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func #to allow auto time stamp
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "Sp00kY"
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collab_project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#creates a local DB within the file structure you can download a SQLite extention in the extension market place.
# When changing the db or adding columns you'd need to run this code flask db migrate ---> flask db upgrade in succession this will make the changes 
migrate = Migrate(app, db)

 ######################
########################
##                    ##
##  Data Base Models  ##
##                    ##
########################
 ######################

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    security_answer1 = db.Column(db.String(200)) 
    security_answer2 = db.Column(db.String(200))
    security_answer3 = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=func.now()) #auto time stamp
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())  #auto time stamp

    # def __repr__(self):
    #     return '<User %r>' % self.username

 ######################
########################
##                    ##
##   Routes go here   ##
##                    ##
########################
 ######################

@app.route("/")
def home_page():

    return render_template('index.html')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route("/register", methods=['POST'])
def add_user_to_db():
    validation = True
    if len(request.form['fname']) < 1:
        validation = False
        flash("Please enter a first name")

    if len(request.form['lname']) < 1:
        validation = False
        flash("Please enter a last name")

    if not EMAIL_REGEX.match(request.form['email']):
        validation = False
        flash("Invalid email address")

    if len(request.form['password']) < 8:
        validation = False
        flash("Please enter a Valid 8 or more characters ")

    if request.form['password'] != request.form['confirm_password']:
        is_valid = False
        flash("Passwords need to match")

    if validation:
        pw_hash = bcrypt.generate_password_hash(request.form['password']) #hashes the password
        new_user = User(first_name = request.form['fname'],
                                     last_name = request.form['lname'],
                                     email = request.form['email'], 
                                     password = pw_hash) #stores all data into this variable new_user
        db.session.add(new_user) #adds the user
        db.session.commit() #commits it to the database
        flash("User added")
    return redirect('/')

@app.route("/Login", methods=['POST'])
def user_login():

    instance_of_user = User.query.filter_by(email=request.form['login_email']).first()
    print(instance_of_user)
    if instance_of_user:
        pw = bcrypt.check_password_hash(instance_of_user.password, request.form['login_password'])
        if pw:
            session['user_id'] = instance_of_user.id
            session['user_greeting'] = instance_of_user.first_name
            return redirect('/usr_home')

        else:
            flash('Invalid user name or password')
            return redirect('/')


@app.route("/usr_home")
def user_homepage():


    return render_template('user_home.html')





if __name__ == "__main__":
        app.run(debug=True)