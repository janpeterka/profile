import os

UPLOAD_FOLDER = 'tmp'

SECRET_KEY = os.environ.get('SECRET_KEY')

SQLALCHEMY_TRACK_MODIFICATIONS = False
# DB_STRING = os.environ.get('DB_STRING')
SQLALCHEMY_DATABASE_URI = os.environ.get('DB_STRING')

TEMPLATES_AUTO_RELOAD = True

# MAIL_SERVER = 'smtp.googlemail.com'
# MAIL_PORT = 465
# MAIL_USE_TLS = False
# MAIL_USE_SSL = True
# MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
# MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
