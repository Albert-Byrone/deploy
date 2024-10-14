import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

# print("Starting", os.environ.get('SQLALCHEMY_DATABASE_URI'))
# print("Starting", os.environ['SQLALCHEMY_DATABASE_URI'])



class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.environ.get('SECRET_KEY')
