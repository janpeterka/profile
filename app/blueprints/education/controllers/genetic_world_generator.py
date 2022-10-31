# import json

from flask import session, redirect, url_for
from flask import render_template as template

from flask_classful import FlaskView

from ..models.world import World

import jsonpickle


class WorldView(FlaskView):
    def before_request(self, name):
        # session.pop("world")
        # try to load world from session
        world_from_session = session.get("world")
        if world_from_session is not None:
            self.world = jsonpickle.decode(world_from_session)
        else:
            self.world = World(size=20)

        # save totals across steps
        if not session.get("total_resources_scores"):
            session["total_resources_scores"] = {"0": "0"}
        # print(session["total_resources_scores"])

    def after_request(self, name, response):
        session["world"] = jsonpickle.encode(self.world)

        # print(name)
        if name in ("add_generation", "next_generation"):
            curr_len = len(session.get("total_resources_scores"))
            session["total_resources_scores"][
                str(curr_len)
            ] = f"{self.world.score.total_resources}"
        # print(session.get("total_resources_scores"))
        return response

    def index(self):
        # from flask_charts import Chart

        # my_chart = Chart("LineChart", "my_chart")
        # my_chart.data.add_column("number", "vol")
        # my_chart.data.add_column("number", "value")

        total_resources_scores = session.get("total_resources_scores")

        if total_resources_scores:
            for i in range(len(total_resources_scores)):
                my_chart.data.add_row([str(i), total_resources_scores[str(i)]])

        return template(
            "education/genetic_world_generator.html.j2",
            world=self.world,
            # chart=my_chart,
        )

    # def before_new_world(self):

    def new_world(self):
        try:
            session.pop("world")
        except Exception:
            pass

        session["world"] = None

        try:
            session.pop("total_resources_scores")
        except Exception:
            pass

        session["total_resources_scores"] = {}
        self.world = World(20)

        return redirect(url_for("WorldView:index"))

    def add_generation(self):
        self.world.add_generation(first=True)
        return redirect(url_for("WorldView:index"))

    def next_generation(self):
        print("mutate")
        self.world.mutate()
        print("select_fittest")
        self.world.select_fittest()
        print("add_generation")
        self.world.add_generation()
        print("done")
        return redirect(url_for("WorldView:index"))

    # def select_fittest(self):
    #     self.world.select_fittest()
    #     return redirect(url_for("WorldView:index"))
