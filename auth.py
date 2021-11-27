from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route("/" ,methods=["GET", "POST"])
def login():
    return render_template('login.html')
    # return "<p>Hello, World!</p>"

@auth.route("/cadastro" ,methods=["GET", "POST"])
def Cadastro():
    # return "Cadastro"
    return render_template('index.html')

@auth.route("/info" ,methods=["GET", "POST"])
def info():
    return render_template('info.html')
    # return "Cadastro realizado com sucesso"

@auth.route('/signup',methods=["GET", "POST"])
def signup_post():
    return render_template('signup.html')
    # email = request.form.get('email')
    # name = request.form.get('name')
    # password = request.form.get('password')

    # user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    # if user: # if a user is found, we want to redirect back to signup page so user can try again
    #     return redirect(url_for('auth.signup'))

    # # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    # new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # # add the new user to the database
    # db.session.add(new_user)
    # db.session.commit()

    # if user: # if a user is found, we want to redirect back to signup page so user can try again
    #     flash('Email address already exists')
    #     return redirect(url_for('auth.signup'))

    # return redirect(url_for('auth.login'))