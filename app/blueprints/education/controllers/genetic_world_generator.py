# import json

from flask import session, redirect, url_for
from flask import render_template as template

from flask_classful import FlaskView

from ..models.world import World

import jsonpickle


class WorldView(FlaskView):
    def before_request(self, name):
        # try to load world from session
        world_from_session = session.get("world")
        if world_from_session is not None:
            self.world = jsonpickle.decode(world_from_session)
        else:
            self.world = World(size=20)

        # save totals across steps
        if session.get("total_resources_scores") is None:
            session["total_resources_scores"] = {}

        print(session.get("total_resources_scores"))

    def after_request(self, name, response):
        session["world"] = jsonpickle.encode(self.world)
        session["total_resources_scores"][
            str(len(session["total_resources_scores"]) + 1)
        ] = self.world.score.total_resources
        return response

    def index(self):
        return template("education/genetic_world_generator.html.j2", world=self.world)

    def before_new_world(self):
        session.pop("world")
        session.pop("total_resources_scores")

    def new_world(self):
        self.world = World(20)
        return redirect(url_for("WorldView:index"))

    def add_generation(self):
        self.world.add_generation(first=True)
        return redirect(url_for("WorldView:index"))

    def next_generation(self):
        self.world.select_fittest()
        self.world.add_generation()
        return redirect(url_for("WorldView:index"))

    # def select_fittest(self):
    #     self.world.select_fittest()
    #     return redirect(url_for("WorldView:index"))
