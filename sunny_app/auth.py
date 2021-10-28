from flask import Blueprint, redirect, url_for, request
from flask.templating import render_template


auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    email = request.form.get("email")
    password1 = request.form.get("password1")
    return render_template("login.html")

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
  email = request.form.get("email")
  username = request.form.get("username")
  password1 = request.form.get("password1")
  password2 = request.form.get("password2")

  return render_template("signup.html")

@auth.route("/logout")
def log_out():
  return redirect(url_for("views.home"))