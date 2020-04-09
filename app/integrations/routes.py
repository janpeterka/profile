#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Blueprint

# from flask import request, redirect, url_for

# from flask import render_template as template
# from flask import current_app as application

from app.integrations.connectors.toggl import TogglConnector

# from google_fit import GoogleFitConnector

integrations_blueprint = Blueprint("integrations", __name__, url_prefix="/integrations")


# TOGGL
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