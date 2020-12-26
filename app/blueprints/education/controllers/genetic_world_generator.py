# import json

# from flask import jsonify, request, abort
from flask import render_template as template

from flask_classful import FlaskView

from ..models.world import World


class WorldView(FlaskView):
    def index(self):
        world = World(size=20)
        return template("education/genetic_world_generator.html.j2", world_html=world.html)

    # def generate_world(self):
    #     world = World(size=20)
    #     return world