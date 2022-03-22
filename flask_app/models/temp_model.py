# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL


class Temp:
    pass
    # Change Database for this model
    # db = "database HERE"

    # def __init__(self, data):
    #     self.id = data['id']
    #     self.first_name = data['first_name']
    #     self.last_name = data['last_name']
    #     self.email = data['email']
    #     self.created_at = data['created_at']
    #     self.updated_at = data['updated_at']

    # UPDATE methods

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
    # def create_new_user(cls, data):
    #     query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
    #     results = connectToMySQL(cls.db).query_db(query, data)
    #     return results

    # @classmethod
    # def get_one_user(cls, data):
    #     query = "SELECT * FROM users WHERE id = %(user_id)s;"
    #     results = connectToMySQL(cls.db).query_db(query, data)
    #     return cls(results[0])

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
