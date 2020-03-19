#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Blueprint

# from flask import request, redirect, url_for

# from flask import render_template as template
# from flask import current_app as application

from app.integrations.connectors.toggl import TogglConnector

# from google_fit import GoogleFitConnector

integrations_blueprint = Blueprint("integrations", __name__, url_prefix="/integrations")


# MAIN
@integrations_blueprint.route("/", methods=["GET"])
def show():
    return "hello world"


@integrations_blueprint.route("/toggl", methods=["GET"])
def show_toggl():
    return "hello toggl"


@integrations_blueprint.route("/<secret_key>/toggl/current")
def toggl_current(secret_key):
    connector = TogglConnector(secret_key)
    response = connector.get_current_time_entry()
    return response


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
