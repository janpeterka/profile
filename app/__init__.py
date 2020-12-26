from flask import Flask

# from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore

from flask_charts import GoogleCharts


# mail = Mail()
db = SQLAlchemy()
migrate = Migrate()
security = Security()
charts = GoogleCharts()


from app.blueprints.auth.models.roles import Role
from app.blueprints.auth.models.users import User

user_datastore = SQLAlchemyUserDatastore(db, User, Role)


def create_app():
    application = Flask(__name__, instance_relative_config=True)

    # CONFIG
    application.config.from_object("config")
    # application.secret_key = application.config['SECRET_KEY']

    # LOGGING
    # from app.config_logging import file_handler
    # application.logger.addHandler(file_handler)

    # from app.config_logging import mail_handler
    # application.logger.addHandler(mail_handler)

    # from app.config_logging import db_handler
    # application.logger.addHandler(db_handler)
    from app.config_logging import gunicorn_logger

    application.logger.addHandler(gunicorn_logger)

    # APPS
    # mail.init_app(application)
    db.init_app(application)
    migrate.init_app(application, db)
    security.init_app(application, user_datastore)
    charts.init_app(application)

    # MODULES
    # Auth module
    from app.blueprints.auth import create_module as auth_create_module

    auth_create_module(application)

    # Main module
    from app.blueprints.main import create_module as main_create_module

    main_create_module(application)

    # Poetry module
    from app.blueprints.poetry import create_module as poetry_create_module

    poetry_create_module(application)

    # Integrations module
    from app.blueprints.integrations import create_module as integrations_create_module

    integrations_create_module(application)

    # Education module
    from app.blueprints.education import create_module as education_create_module

    education_create_module(application)

    # Errors module
    from app.errors import create_module as errors_create_module

    errors_create_module(application)

    return application
