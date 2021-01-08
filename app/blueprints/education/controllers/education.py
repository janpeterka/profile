#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
# from flask import redirect

# from flask import render_template as template

# from flask_security import current_user, login_required

# from .connectors.toggl import TogglConnector
# from .connectors.exist import ExistConnector

# from ..models.tokens import Token
# from ..models.services import Service

education_blueprint = Blueprint("education", __name__, url_prefix="/education")
