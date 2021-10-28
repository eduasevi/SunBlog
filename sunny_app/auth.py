from flask import Blueprint, redirect, url_for, request, flash
import flask
from flask.templating import render_template
from sqlalchemy.sql.functions import user
from . import db 
from .models import User


auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    email = request.form.get("email")
    password1 = request.form.get("password1")
    return render_template("login.html")

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
  if request.method == 'POST':
    email = request.form.get("email")
    username = request.form.get("username")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")

  email_exists = User.query.filter_by(email=email).first()
  username_exists = User.query.filter_by(username=username).first()
  if email_exists:
    flash('Email is already in use.', category='error')
  elif username_exists:
    flash('Username already in use. Please log in.', category='error')
  elif password1 != password2:
    flash('Passwords don\'t match!', category='error')
  elif len(username) < 2:
    flash('Username is too short', category='error')
  elif len(password1) < 6:
    flash('Password needs to be longer than six characters', category='error')
  elif len(email) < 4:
    flash('Email is invalid', category='error')
  else:
    new_user = User(email=email, username=username, password=password1)
    db.session.add(new_user)
    db.session.commit()
    flash('Welcome! New User Created.')
    return redirect(url_for('views.home'))

  return render_template("signup.html")

@auth.route("/logout")
def log_out():
  return redirect(url_for("views.home"))