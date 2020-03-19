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

        self.known_tasks = {
            "workout": "body",
            "yoga": "body",
            "running": "body",

            "cleaning": "maintenance"
        }

        self.projects = {
            "meditation": os.environ.get("TOGGL_PID_MEDITATION"),
            "body": os.environ.get("TOGGL_PID_BODY"),
            "gaming": os.environ.get("TOGGL_PID_GAMING"),
            "distraction": os.environ.get("TOGGL_PID_DISTRACTION"),
            "leisure": os.environ.get("TOGGL_PID_LEISURE"),
            "maintenance": os.environ.get("TOGGL_PID_MAINTENANCE"),
        }

    def full_url(self):
        return self.url + self.api_url

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
        self.api_url = "/api/v8/time_entries/current"
        response = requests.get(self.full_url())
        response = json.loads(response.text)

        if "data" in response:
            response = response["data"]
        else:
            response = None

        return response

    def start_time_entry(self, project_name, entry_name=None):
        self.api_url = "/api/v8/time_entries/start"

        if project_name and project_name in self.projects:
            project_id = int(self.projects[project_name])
        elif project_name and project_name in self.known_tasks:
            entry_name = project_name
            project_id = int(self.projects[self.known_tasks[project_name]])
        else:
            project_id = None
            if entry_name is None:
                entry_name = project_name

        if entry_name is None:
            entry_name = ""

        data = {}
        data["time_entry"] = {}
        data["time_entry"]["description"] = entry_name
        data["time_entry"]["created_with"] = "profile_integrations"

        if project_id is not None:
            data["time_entry"]["pid"] = project_id

        response = requests.post(self.full_url(), json=data)
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
