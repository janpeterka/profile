import logging

# Gunicorn error logger
gunicorn_logger = logging.getLogger("profile.error")
gunicorn_logger.setLevel(logging.WARNING)
