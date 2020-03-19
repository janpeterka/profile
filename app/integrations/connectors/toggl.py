import requests
import os
import json
from flask import jsonify

from app.integrations.connectors.connector import Connector


class TogglConnector(Connector):
    def __init__(self, secret_key):

        super(TogglConnector, self).__init__(secret_key)

        self.service_url = "www.toggl.com"
        self.api_token = os.environ.get("TOGGL_API_TOKEN")

        self.url = "https://" + self.api_token + ":api_token" + "@" + self.service_url

        self.projects = {
            "meditation": os.environ.get("TOGGL_PID_MEDITATION"),
            "body": os.environ.get("TOGGL_PID_BODY"),
            "other": None,
        }

    # general methods
    def create_time_entry(self, project_name, entry_name):
        pass

    def get_current_time_entry_id(self):
        current_time_entry = self.get_current_time_entry()
        if current_time_entry and "id" in current_time_entry:
            return current_time_entry["id"]
        else:
            return None

    def get_current_time_entry(self):
        api_url = "/api/v8/time_entries/current"
        response = requests.get(self.url + "/" + api_url)
        response = json.loads(response.text)
        # WIP - if returns null
        try:
            response = response["data"]
        except Exception:
            response = None

        return response

    def start_time_entry(self, project_name="other", entry_name=""):
        api_url = "/api/v8/time_entries/start"

        project_id = int(self.projects[project_name])

        data = {}
        data["time_entry"] = {}
        data["time_entry"]["description"] = entry_name
        data["time_entry"]["created_with"] = "profile_integrations"

        if project_id is not None:
            data["time_entry"]["pid"] = project_id

        response = requests.post(self.url + api_url, json=data)
        return response.text

    def stop_time_entry(self, time_entry_id=None):
        if time_entry_id is None:
            time_entry_id = self.get_current_time_entry_id()

        if time_entry_id is None:
            return "No entry running"

        api_url = "/api/v8/time_entries/{}/stop".format(time_entry_id)

        response = requests.put(self.url + api_url)
        return "Entry stopped"

    # output integrations
    def get_data_for_google_fit():
        pass
