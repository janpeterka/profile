#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from datetime import date
# import math
# import os

from flask import Blueprint
# from flask import request, redirect, url_for

# from flask import render_template as template
# from flask import current_app as application

# from toggl import TogglConnector
# from google_fit import GoogleFitConnector

integrations_blueprint = Blueprint("integrations", __name__)


# MAIN
@integrations_blueprint.route("/", methods=["GET"])
def show():
    return "hello world"
