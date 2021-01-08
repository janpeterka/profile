#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import json

from flask import Blueprint

# from flask import session, redirect, url_for
# from flask import render_template as template
from flask_classful import FlaskView

blog_blueprint = Blueprint("blog", __name__, url_prefix="/blog")


class BlogView(FlaskView):
    pass
