from flask import Flask
# from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate


# mail = Mail()
db = SQLAlchemy()
# migrate = Migrate()


def create_app():
    application = Flask(__name__, instance_relative_config=True)

    # CONFIG
    application.config.from_object('config')
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
    # migrate.init_app(application, db)

    # MODULES

    # Main module
    from app.main import create_module as main_create_module
    main_create_module(application)

    # Bunkrs module
    from app.bunkrs import create_module as bunkrs_create_module
    bunkrs_create_module(application)

    # Movie module
    from app.movie import create_module as movie_create_module
    movie_create_module(application)

    # Finance module
    from app.finance import create_module as finance_create_module
    finance_create_module(application)

    # Errors module
    from app.errors import create_module as errors_create_module
    errors_create_module(application)

    # Support module
    # from app.support import create_module as support_create_module
    # support_create_module(application)

    return application
