from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"

        results = connectToMySQL(DATABASE).query_db(query)

        emails = []
        for result in results:
            emails.append(cls(result))
        
        return emails

    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM emails WHERE email = %(email)s"

        results =  connectToMySQL(DATABASE).query_db(query, data)

        if results:
            return cls(results[0])
        
        return False

    @classmethod
    def create(cls,data):
        query = "INSERT INTO emails (email) VALUES (%(email)s)"

        return connectToMySQL(DATABASE).query_db(query,data)
        

    @classmethod
    def delete(cls,data):
        query = """DELETE FROM emails WHERE id = %(id)s"""
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def  validate_email(form):
        is_valid = True

        if not EMAIL_REGEX.match(form["email"]):
            print("validate_email: not a valid email!")
            flash("Please enter a valid email.")
            is_valid = False

        if Email.get_one_by_email(form):
            flash("Email already taken")
            is_valid = False
            



        return is_valid