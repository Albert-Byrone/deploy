# Introduction to Flask
import json

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
import requests
import jwt
import datetime
# from flask_restful import Resource, Api
# from  forms import UserRegistrationForm

# from models import Post


from config import Config

app = Flask(__name__)
app.config.from_object(Config)
# secret = app.config["SECRET_KEY"]

# print("secret", secret)

# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
# api = Api(app) # Instance of Flask-Rest

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password'] # qwery12

    # Check if the username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "username already exists"}), 400
    # add the user infomation to the database
    hash_password = bcrypt.generate_password_hash(password) # orj5hyyu853408549783546904-0kpogjhotj
    new_user = User(username=username, password=hash_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password'] # qwery12

    user = User.query.filter_by(username=username).first()

    if not user or not bcrypt.check_password_hash(user.password, password): # returns True
        return jsonify({ "message": "Invalide credentials"}),401

    token = jwt.encode({"user_id": user.id, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config["SECRET_KEY"], algorithm="HS256")
    return jsonify({ "token": token})

@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({ "message": "Token is missing"})

    try:
        token =token.split()[1]
        if token:
            decoded_token =  jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            user_id=decoded_token["user_id"]

            user =User.query.get(user_id)

            return jsonify({ "message": f"Welcome , {user.username}", "user_id": user.id})
        else:
            return jsonify({ "message": "Token is invalid"})
    except jwt.InvalidTokenError:
        return jsonify({ "message": "Token is invalid"})





if __name__ == '__main__':
    app.run(host="0.0.0.0")


# def find_book(book_id):
#     for book in books:
#         if book['id'] == book_id:
#             return book
#         return None
# # Single book
# class Book(Resource):
#     def get(self, book_id): # Get a single book
#         book = find_book(book_id)
#         if book:
#             return book, 200 # Return the book with a status code of 200(OK)
#         return {'message': 'No book found with that ID'}, 404
#
#     def put(self, book_id): # Get a single book
#         book = find_book(book_id)
#         if book:
#             data = request.json
#             book.update({
#                 "title": data['title'], # data.get('title')
#                 "author": data['author'], # data.get('author')
#             })
#             return book, 200 # Return the book with a status code of 200(OK)
#         return {'message': 'No book found'}, 404

# class BookList(Resource):
#     def get(self):
#         return books, 200
#
#     def post(self):
#         data = request.json
#         new_book = {
#             "id": len(books) + 1,
#             "title": data['title'],
#             "author": data['author']
#         }
#         books.append(new_book)
#         return new_book, 201 # Created successfully

# @app.route('/posts', methods=['POST'])
# def create_post():
#     print(request)
#     data = request.json
#     new_post = Post(title= data["title"], description=data["description"])
#     db.session.add(new_post)
#     db.session.commit()
#     return jsonify(new_post.to_dict()), 201

# http://127.0.0.1:5000/books
# api.add_resource(BookList, '/books')
# api.add_resource(Book, '/books/<int:book_id>')


# Bookstore API
# Client- server -- Database ( Books/Users)
# https:localhost:3000/books URL
# Add a new post
# http://127.0.0.1:5000/posts  POST

# # Get  all posts
# @app.route('/posts', methods=['GET'])
# def get_posts():
#     posts = Post.query.all()
#     print("===", posts)
#     return jsonify([post.to_dict() for post in posts]), 200

# Update a post
# Delete a post

# Import models
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80))
#     name = db.Column(db.String(80), unique=True, nullable=False, default="Albert)
#     description = db.Column(db.String(200))
#
#     def to_dict(self):
#         return {
#             "id": self.id,
#             "title": self.title,
#             "description": self.description
#         }


# Constraints
# Rules enforced within the database level that defines the wide range of operations,
# Common database constrains include the following:
# Primary Key - Ensures that each record in a table is unique and identifies a particular row
# Foreign key - Ensures that value in the column( a set of column) matches a value in another table , maintaining referential integrity
# between tables
# Unique Constraint - Ensures that all value in a column(a set of column) is unique
# Not Null Constraint - Ensures that a column cannot have a null value
# Default Constraint - Provide a default value for the column when no value is provided

# Validations -- enforced within the application level to ensure that the data is correct and meaningful before
# is sent to the database

# WTForms for validations


# JWT(JSON Web Token) = a small package of information(token) that is created and send to the user after a suucessfull login
# ID == prove who they you are


# How does it work?
# 1. User logs in:
# - You can enter your username/email and password in the application
# - The application checks if the information is correct
# - if the information is correct then the app creates the JWT and sends back to
# if you:
#
#     - The JWT contains certain information:
#     - user-id
#     - time you want the JWT to be expire