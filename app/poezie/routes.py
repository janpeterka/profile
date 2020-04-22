#!/usr/bin/env python
# -*- coding: utf-8 -*-
# run by pyserver

import os
from flask import Blueprint

from flask import redirect, url_for, request

from flask import render_template as template
from app.poezie.models import Poezie

BLUEPRINT_ROOT = os.path.dirname(os.path.realpath(__file__))

poezie_blueprint = Blueprint("poezie", __name__)


@poezie_blueprint.route("/poezie", methods=["GET"])
@poezie_blueprint.route("/poezie/", methods=["GET"])
def index():
    return template("poezie/index.html.j2")


@poezie_blueprint.route("/poezie/show/<id>", methods=["GET"])
def show(id):
    item = Poezie.load(id)
    return template("poezie/show.html.j2", poezie=item)


@poezie_blueprint.route("/poezie/post", methods=["POST"])
def post():
    poezie = Poezie(
        name=request.form.get("name"),
        created_by=request.form.get("author"),
        latitude=request.form.get("coords_x"),
        longitude=request.form.get("coords_y"),
    )
    print(poezie)
    print(poezie.name)

    poezie.save()
    print(poezie.id)
    return redirect("poezie/show/" + poezie.id)
