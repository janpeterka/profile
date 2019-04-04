from flask import request, redirect

from app import create_app

from app.models import db

# from app.data import template_data

application = create_app()
