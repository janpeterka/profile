#!/usr/bin/env python
# -*- coding: utf-8 -*-
# run by pyserver


import os
from flask import Blueprint

from flask import render_template as template
# from flask import request, redirect
# from flask import jsonify
from flask import send_file
# from flask import abort

# from flask import current_app as application

# import requests
# import json

from app import models

from pathlib import Path
# import subprocess
import ffmpeg


BLUEPRINT_ROOT = os.path.dirname(os.path.realpath(__file__))
SONGBOOKS_DIR = os.path.join(BLUEPRINT_ROOT, '../public/songbooks/')
MMS_DIR = os.path.join(BLUEPRINT_ROOT, '../public/mms/')

main_blueprint = Blueprint('main', __name__)


# MAIN
@main_blueprint.route('/', methods=['GET'])
def main():
    return template('dashboard.tpl')


@main_blueprint.route('/newsletter', methods=['GET'])
def show_newsletter():
    return template('newsletter_subscribe.html.j2')


@main_blueprint.route('/portfolio', methods=['GET'])
def show_portfolio():
    return template('portfolio.tpl')


@main_blueprint.route('/songbooks', methods=['GET'])
@main_blueprint.route('/zpevniky', methods=['GET'])
def show_songbooks():
    folders = []
    for folder in os.walk(SONGBOOKS_DIR):
        if os.path.isdir(folder[0]):
            folders.append(models.Folder(folder[0]))

    if len(folders) > 0:
        del folders[0]

    for folder in folders:
        folder.name = Path(folder.path).name

    folders.sort(key=lambda x: x.name, reverse=False)

    return template('songbooks.tpl', folders=folders)


@main_blueprint.route('/songbooks/<filename>', methods=['GET'])
def download_songbook_file(filename):
    return send_file(SONGBOOKS_DIR + filename.split('.')[0] + "/" + filename,
                     attachment_filename=filename)


@main_blueprint.route('/pexeso', methods=['GET'])
def show_pexeso():
    return template('pexeso.tpl')
