#!/usr/bin/env python
# -*- coding: utf-8 -*-
# run by pyserver

import os
from flask import Blueprint

from flask import redirect, url_for, request

from flask import render_template as template
from app.poezie.models import Poezie
from app.poezie.forms import PoezieForm

from app.helpers.form import save_form_to_session, create_form

BLUEPRINT_ROOT = os.path.dirname(os.path.realpath(__file__))

poezie_blueprint = Blueprint("poezie", __name__)


@poezie_blueprint.route("/poezie", methods=["GET"])
@poezie_blueprint.route("/poezie/", methods=["GET"])
def index():
    form = create_form(PoezieForm)
    return template("poezie/index.html.j2", form=form)


@poezie_blueprint.route("/poezie/show/<id>", methods=["GET"])
def show(id):
    item = Poezie.load(id)

    return template("poezie/show.html.j2", poezie=item)


@poezie_blueprint.route("/poezie/post", methods=["POST"])
def post():
    form = PoezieForm(request.form)
    if not form.validate_on_submit():
        save_form_to_session(request.form)
        return redirect(url_for("DietsView:new"))

    # save photo
    # 
    # 
    poezie = Poezie(
        name=request.form.get("name"),
        created_by=request.form.get("created_by"),
        latitude=request.form.get("latitude"),
        longitude=request.form.get("longitude"),
        # photo_path=
    )
    poezie.save()
    return redirect("show/" + str(poezie.id))
