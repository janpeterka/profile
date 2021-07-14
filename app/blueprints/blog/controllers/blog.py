#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import json
import os

from flask import Blueprint

# from flask import session, redirect, url_for
from flask import render_template as template
from flask_classful import FlaskView

blog_blueprint = Blueprint("blog", __name__, url_prefix="/blog")
BLUEPRINT_ROOT = os.path.dirname(os.path.realpath(__file__))


class BlogView(FlaskView):
    pass


#     @blog_blueprint.route("/blog", methods=["GET"])
#     @blog_blueprint.route("/blog/", methods=["GET"])
# def index(self):
#         return ("ok")
#         return(template("blog/blog.html.j2"))
#
#
@blog_blueprint.route("/", methods=["GET"])
# @blog_blueprint.route("/blog", methods=["GET"])
# @blog_blueprint.route("/blog/", methods=["GET"])
def index():
    from os import listdir
    from os.path import isfile, join

    mypath = os.path.join(BLUEPRINT_ROOT, "../../../templates/blog/articles/")
    files = [f for f in listdir(os.path.dirname(mypath)) if isfile(join(mypath, f))]
    # print(files)
    articles = files

    return template("blog/blog.html.j2", articles=articles)
