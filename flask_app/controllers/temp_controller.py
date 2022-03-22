from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.temp_model import Temp


# * ===========================================
# ? RENDER / index
# * ===========================================
@app.route('/')
def users():

    print("Where...HOME--READ")
    return render_template("index.html")


# * ===========================================
# ? RENDER / Create
# * ===========================================


# t- ===========================================
# ? PROCESS FORM - / Create_new
# t- ===========================================
