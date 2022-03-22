from crypt import methods
from flask_app.models.users_model import User
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


# * ===========================================
# ? RENDER / index
# * ===========================================
@app.route('/')
def users():

    print("=== HOME ===")
    return render_template("index.html")


# t- ===========================================
# ? PROCESS FORM - / Create_new
# t- ===========================================
@app.route("/register_user", methods=["POST"])
def register_user():

    #   Validate form
    if not User.validate_registration(request.form):
        return redirect("/")

    #   encrypt password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    #   gather form info for query
    query_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash
    }

    #   run Insert query and return user_id
    user_id = User.create_new_user(query_data)

    #   assign user_id to session
    session["user_id"] = user_id
    #   redirect...
    return redirect("/dashboard")


# t- ===========================================
# ? PROCESS FORM - / Login
# t- ===========================================
@app.route("/login_user", methods=["POST"])
def login_user():

    # validate info
    if not User.validate_login(request.form):
        return redirect("/")

    # query based on form data
    query_data = {
        "email": request.form["email"]
    }

    logged_in_user = User.get_by_email(query_data)

    # put user_id into session
    session["user_id"] = logged_in_user.id

    # redirect
    return redirect("/dashboard")


# * ===========================================
# ? RENDER / Dashboard
# * ===========================================


# * ===========================================
# ? RENDER / Create
# * ===========================================


# t- ===========================================
# ? PROCESS FORM - / Create_new
# t- ===========================================
