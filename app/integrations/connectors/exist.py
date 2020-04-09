import requests
import datetime

from app.integrations.connectors.connector import Connector

from app.integrations.connectors.toggl import TogglConnector


class ExistConnector(Connector):
    def __init__(self, secret_key):
        super(ExistConnector, self).__init__(secret_key)
        self.secret_key = secret_key

    def do_request(self, request_type="get", headers=None, json=None):
        if not headers:
            headers = {"Authorization": "Bearer {}".format(self.api_token)}

        if request_type == "get":
            response = requests.get(self.api, headers=headers, json=json)
        elif request_type == "post":
            response = requests.post(self.api, headers=headers, json=json)

        return response

    def add_daily_data(self):
        toggl_connector = TogglConnector(self.secret_key)
        # Get toggl daily entries
        entries = toggl_connector.get_todays_time_entries()
        attributes = self.toggl_entries_to_exist_attributes(entries)
        for attribute in attributes:
            self.add_attribute(attribute)

        return "synchronized"

    def add_attribute(self, attribute):
        self.api = "https://exist.io/api/1/attributes/custom/append/"

        data = {}
        data["value"] = attribute
        data["date"] = datetime.date.today().isoformat()

        response = requests.post(self.api, json=data)
        response = self.do_request("post", json=data)

        if response.status_code == requests.codes.ok:
            return response.text
        else:
            return False

    def toggl_entries_to_exist_attributes(self, entries):

        attributes = []

        entry_to_attribute = {
            "audiobook": "a audiobook",
            "distraction": "a distraction",
            "game": "a gaming",
            "gaming": "a gaming",
            "guitar": "a guitar",
            "meditation": "a meditation",
            "movie": "a movie",
            "piano": "a piano",
            "podcast": "a podcast",
            "keto": "a programming",
            "sborio": "a programming",
            "profile": "a programming",
            "programming": "a programming",
            "reading": "a reading",
            "reading articles": "a reading articles",
            "yoga": "a sport yoga",
            "workout": "a sport workout",
            "walk": "a walk",
            "nap": "sleep nap",
        }

        for entry in entries:
            for key, value in entry_to_attribute.items():
                if key in entry:
                    attributes.append(value)

        return attributes
