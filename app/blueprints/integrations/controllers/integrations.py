#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

from .connectors.toggl import TogglConnector
from .connectors.exist import ExistConnector

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


@integrations_blueprint.route("/<secret_key>/exist/daily")
def exist_daily(secret_key):
    connector = ExistConnector(secret_key)
    return connector.add_daily_data()
