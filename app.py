#!/usr/bin/env python
# -*- coding: utf-8 -*-

# run by pyserver

from flask import Flask, render_template as template
# from flask import request, redirect
# from flask import flash
from flask import send_from_directory, send_file

# from werkzeug import SharedDataMiddleware

import os
from pathlib import Path

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

# app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {'/': os.path.join(os.path.dirname(__file__), 'public')})

# SRCDIR = os.path.dirname(os.path.abspath(__file__))
DATADIR = os.path.join(PROJECT_ROOT, 'public/songbooks/')


class Folder(object):
    def __init__(self, path, name=None):
        self.path = path
        self.name = name


@app.route('/', methods=['GET'])
def main():
    return template('dashboard.tpl')


@app.route('/songbooks', methods=['GET'])
@app.route('/zpevniky', methods=['GET'])
def showSongbooks():
    folders = []
    for folder in os.walk(DATADIR):
        folders.append(Folder(folder[0]))

    del folders[0]

    for folder in folders:
        folder.name = Path(folder.path).name

    folders.sort(key=lambda x: x.name, reverse=False)

    return template('songbooks.tpl', folders=folders)


@app.route('/<name>', methods=['GET'])
def showFile(name):
    return send_file(DATADIR + name.split('.')[0] + '/' + name, attachment_filename=name)


@app.route('/portfolio', methods=['GET'])
def showPortfolio():
    return template('portfolio.tpl')


# ERROR
@app.errorhandler(404)
def error404(error):
    return 'Tady nic není (Err404)'


@app.errorhandler(500)
def error500(error):
    return 'Někde se stala chyba (Err500)'


if __name__ == "__main__":
    # app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)
    app.run(debug=True)
