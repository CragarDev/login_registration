# import the function that will return an instance of a connection
import re  # the regex module
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# create a regular expression object that we'll use later
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    # Change Database for this model
    db = "Login_Reg_schema"

    def __init__(self, data):
        self.id = data['id']

        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Validation
    @staticmethod
    def validate_registration(form_data):
        is_valid = True

        if len(form_data["first_name"]) < 2:
            flash("First name must be at least 2 characters in length!")
            is_valid = False

        if len(form_data["last_name"]) < 2:
            flash("Last name must be at least 2 characters in length!")
            is_valid = False

        if not EMAIL_REGEX.match(form_data["email"]):
            flash("Please enter a valid email address!")
            is_valid = False

        if len(form_data["password"]) < 8:
            flash("password must be at least 8 characters in length!")
            is_valid = False

        if form_data["password"] != form_data["password_confirmation"]:
            flash("Password and password confirmation must match!")
            is_valid = False

        if User.get_by_email(form_data):
            flash("Email is already registered, please enter a unique email address")
            is_valid = False

        return is_valid

    @staticmethod
    def validate_login(form_data):
        is_valid = True

        user_from_db = User.get_by_email(form_data)

        if not user_from_db:
            flash("Invalid Email/Password")
            is_valid = False

        elif not bcrypt.check_password_hash(user_from_db.password, form_data["password"]):
            # if we get False after checking the password
            flash("Invalid Email/Password")
            is_valid = False

        return is_valid

    @classmethod
    def create_new_user(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email, password, created_at, updated_at ) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s,  NOW() , NOW() );"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    # @classmethod
    # def get_all_users(cls):
    #     query = "SELECT * FROM users;"
    #     # make sure to call the connectToMySQL function with the schema you are targeting.
    #     results = connectToMySQL(cls.db).query_db(query)
    #     # Create an empty list to append our instances of friends
    #     users = []
    #     # Iterate over the db results and create instances of friends with cls.
    #     for user in results:
    #         users.append(cls(user))
    #     return users

    # @classmethod
    # def update_user(cls, data):
    #     query = "UPDATE users SET first_name = %(first_name)s , last_name = %(last_name)s , email = %(email)s ,updated_at = NOW() WHERE id = %(id)s;"
    #     connectToMySQL(cls.db).query_db(query, data)
    #     return
    # @classmethod
    # def delete_user(cls, data):
    #     query = "DELETE FROM users WHERE id = %(id)s;"
    #     connectToMySQL(cls.db).query_db(query, data)
    #     return
