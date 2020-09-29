#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import redirect

from flask import render_template as template

from flask_security import current_user

from .connectors.toggl import TogglConnector
from .connectors.exist import ExistConnector

from ..models.tokens import Token
from ..models.services import Service

integrations_blueprint = Blueprint("integrations", __name__, url_prefix="/integrations")


@integrations_blueprint.route("/")
def main():
    print(current_user.tokens)
    return template("integrations/main.html.j2")


@integrations_blueprint.route("/add_toggl/<api_key>",)
def add_toggl_key(api_key):
    token = Token()
    token.service = Service.load_by_name("toggl")
    token.value = api_key
    token.user = current_user
    token.save()
    return redirect("/integrations")


# toggl
@integrations_blueprint.route("/<secret_key>/toggl/start/<project_name>")
@integrations_blueprint.route("/<secret_key>/toggl/start/<project_name>/")
@integrations_blueprint.route("/<secret_key>/toggl/start/<project_name>/<entry_name>")
def toggl_start(secret_key, project_name, entry_name=None):
    connector = TogglConnector(secret_key)
    return connector.start_time_entry(project_name=project_name, entry_name=entry_name)


@integrations_blueprint.route("/<secret_key>/toggl/stop")
def toggl_stop(secret_key):
    connector = TogglConnector(secret_key)
    return connector.stop_time_entry()


@integrations_blueprint.route("/<secret_key>/toggl/today")
def toggl_get_todays_entries(secret_key):
    connector = TogglConnector(secret_key)
    return connector.get_todays_time_entries()


# Exist
@integrations_blueprint.route("/<secret_key>/exist/daily")
def exist_daily(secret_key):
    connector = ExistConnector(secret_key)
    return connector.add_daily_data()
