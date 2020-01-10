#!/usr/bin/env python
# -*- coding: utf-8 -*-
# run by pyserver

import os
from flask import Blueprint
from flask import redirect, url_for, send_from_directory

from flask import render_template as template

BLUEPRINT_ROOT = os.path.dirname(os.path.realpath(__file__))

movie_blueprint = Blueprint('movie', __name__)


@movie_blueprint.route('/movie', methods=['GET'])
def show_movie():
    return template('movie/movie.html.j2')


# @movie_blueprint.route('/movie_json', methods=['GET'])
# def show_json():
# 	return send_from_directory('static', filename="js/movie.json")