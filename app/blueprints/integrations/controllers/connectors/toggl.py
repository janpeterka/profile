import requests
import os
import json
import datetime
import urllib.parse

# from flask import jsonify

from .connector import Connector


class TogglConnector(Connector):
    def __init__(self, secret_key):
        super(TogglConnector, self).__init__(secret_key)
        self.service_url = "www.toggl.com"
        self.api_token = self.user.toggl_token
        self.url = "https://" + self.api_token + ":api_token" + "@" + self.service_url

        self.known_tasks = {
            "workout": "body",
            "exercise": "body",
            "yoga": "body",
            "running": "body",
            "writing": "hobby",
            "guitar": "hobby",
            "piano": "hobby",
            "meditation": "meditation",
            "a cleaning": "maintenance",
            "cleaning": "maintenance",
            "nap": "sleep",
        }

        self.projects = {
            "body": os.environ.get("TOGGL_PID_BODY"),
            "distraction": os.environ.get("TOGGL_PID_DISTRACTION"),
            "gaming": os.environ.get("TOGGL_PID_GAMING"),
            "hobby": os.environ.get("TOGGL_PID_HOBBY"),
            "leisure": os.environ.get("TOGGL_PID_LEISURE"),
            "maintenance": os.environ.get("TOGGL_PID_MAINTENANCE"),
            "meditation": os.environ.get("TOGGL_PID_MEDITATION"),
            "movie": os.environ.get("TOGGL_PID_MOVIES"),
            "sleep": os.environ.get("TOGGL_PID_SLEEP"),
        }

    @property
    def full_url(self):
        return self.url + self.api_url

    # general methods
    def get_current_time_entry_id(self):
        current_time_entry = self.get_current_time_entry()
        if current_time_entry and "id" in current_time_entry:
            return current_time_entry["id"]
        else:
            return None

    def get_current_time_entry(self):
        self.api_url = "/api/v8/time_entries/current"
        response = requests.get(self.full_url)
        response = json.loads(response.text)

        if "data" in response:
            response = response["data"]
        else:
            response = None

        return response

    def start_time_entry(self, project_name, entry_name=None):
        self.api_url = "/api/v8/time_entries/start"
        project_name = project_name.strip()
        if entry_name:
            entry_name = entry_name.strip()

        if project_name and project_name in self.known_tasks:
            entry_name = project_name
            project_id = int(self.projects[self.known_tasks[project_name]])
        elif project_name and project_name in self.projects:
            project_id = int(self.projects[project_name])
        elif project_name:
            project_id = None
            if entry_name is None:
                entry_name = project_name
        else:
            project_id = None

        if entry_name is None:
            entry_name = ""

        data = {}
        data["time_entry"] = {}
        data["time_entry"]["description"] = entry_name
        data["time_entry"]["created_with"] = "profile_integrations"

        if project_id is not None:
            data["time_entry"]["pid"] = project_id

        response = requests.post(self.full_url, json=data)
        return response.text

    def stop_time_entry(self, time_entry_id=None):
        if time_entry_id is None:
            time_entry_id = self.get_current_time_entry_id()

        if time_entry_id is None:
            return "No entry running"

        self.api_url = "/api/v8/time_entries/{}/stop".format(time_entry_id)

        response = requests.put(self.full_url)

        if response.status_code == requests.codes.ok:
            return "Entry stopped"
        else:
            return "Something went wrong with request"

    def get_todays_time_entries(self):
        start_datetime = (
            datetime.datetime.utcnow()
            .replace(tzinfo=datetime.timezone.utc)
            .replace(microsecond=0, second=0, minute=0, hour=0)
            .isoformat()
        )

        end_datetime = (
            datetime.datetime.utcnow()
            .replace(tzinfo=datetime.timezone.utc)
            .replace(microsecond=0, second=59, minute=59, hour=23)
            .isoformat()
        )

        start_datetime = urllib.parse.quote(start_datetime)
        end_datetime = urllib.parse.quote(end_datetime)

        self.api_url = "/api/v8/time_entries?start_date={}&end_date={}".format(
            start_datetime, end_datetime
        )

        response = requests.get(self.full_url)

        entries = json.loads(response.text)

        entry_descriptions = []
        for entry in entries:
            entry_descriptions.append(entry["description"])
            # print(entry["description"])

        if response.status_code == requests.codes.ok:
            return entry_descriptions
        else:
            return False

    # output integrations
    def get_data_for_google_fit():
        pass
