import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'thisishardtoguess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
