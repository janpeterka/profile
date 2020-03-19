import os

UPLOAD_FOLDER = "tmp"

SECRET_KEY = os.environ.get("SECRET_KEY")

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ.get("DB_STRING")

TEMPLATES_AUTO_RELOAD = True

APP_STATE = os.environ.get("APP_STATE")
