import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RAPIDAPI_HOST = os.environ.get('RAPIDAPI_HOST')
    RAPIDAPI_KEY = os.environ.get('RAPIDAPI_KEY')