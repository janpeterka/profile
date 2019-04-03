#!/usr/bin/env python
# -*- coding: utf-8 -*-

# run by pyserver

from flask import Flask, render_template as template
# from flask import request, redirect
# from flask import flash
# from flask import send_from_directory
from flask import send_file

# from werkzeug import SharedDataMiddleware

import os
from pathlib import Path

import subprocess

import ffmpeg

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

# app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {'/': os.path.join(os.path.dirname(__file__), 'public')})

# SRCDIR = os.path.dirname(os.path.abspath(__file__))
SONGBOOKS_DIR = os.path.join(PROJECT_ROOT, 'public/songbooks/')
MMS_DIR = os.path.join(PROJECT_ROOT, 'public/mms/')


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
    for folder in os.walk(SONGBOOKS_DIR):
        if os.path.isdir(folder[0]):
            folders.append(Folder(folder[0]))

    del folders[0]

    for folder in folders:
        folder.name = Path(folder.path).name

    folders.sort(key=lambda x: x.name, reverse=False)

    return template('songbooks.tpl', folders=folders)


@app.route('/songbooks/<name>', methods=['GET'])
def downloadSongbookFile(name):
    return send_file(SONGBOOKS_DIR + name.split('.')[0] + "/" + name, attachment_filename=name)


@app.route('/mms2018', methods=['GET'])
@app.route('/mms', methods=['GET'])
def showMMS():

    # Zpracuj soubory do složek - OLD
    # for file in os.listdir(MMS_DIR):
    #     if not os.path.isdir(MMS_DIR + file):  # je to opravdu file
    #         file_path = MMS_DIR + file
    #         file_name = file.split('.')[0]
    #         folder_path = MMS_DIR + file_name + "/"

    #         # print(MMS_DIR + file)
    #         print(folder_path)

    #         # Vytvoř složku
    #         try:
    #             os.mkdir(folder_path)
    #             # print("Created directory {}".format(MMS_DIR + file.split('.')[0]))
    #         except OSError:
    #             print("Cannot create directory {}".format(folder_path))

    #         # Dej do ní soubor
    #         try:
    #             os.rename(file_path, folder_path + file)
    #             # print("Moved {} to {}".format(MMS_DIR + file, MMS_DIR + file.split('.')[0] + "/" + file))
    #         except OSError:
    #             print("Cannot move {} to {}".format(file_path, folder_path + file))

    #         # WIP - udělej konverze

    #         # audio - get mp3
    #         file_audio = getAudio(folder_path + file, file_name)
    #         file_video = getVideo(folder_path + file, file_name)

    # Načti a zobraz složky
    folders = []

    for folder in os.walk(MMS_DIR):
        if os.path.isdir(folder[0]):  # je to opravdu folder
            folders.append(Folder(folder[0]))

    del folders[0]

    for folder in folders:
        folder.name = Path(folder.path).name

    folders.sort(key=lambda x: x.name, reverse=False)

    return template('mms.tpl', folders=folders)


@app.route('/mms/<name>', methods=['GET'])
def downloadMMSFile(name):
    return send_file(MMS_DIR + name.split('.')[0] + "/" + name, attachment_filename=name)


def getVideo(file, file_name, file_format="flv"):
    stream = ffmpeg.input(file)
    # stream = ffmpeg.hflip(stream)

    stream = ffmpeg.output(stream, MMS_DIR + file_name + "/" + file_name + '.' + file_format)

    ffmpeg.run(stream)


def getAudio(file, file_name, file_format='mp3'):

    # ffmpeg -i ~/Dropbox/Programming/profile/public/mms/test/test.mkv -vn -c:a libmp3lame -y ~/Dropbox/Programming/profile/public/mms/test/test.mp3

    stream = ffmpeg.input(file)
    # stream = ffmpeg.hflip(stream)

    print(MMS_DIR + file_name + "/" + file_name + '.' + file_format)

    stream = ffmpeg.output(stream, MMS_DIR + file_name + "/" + file_name + '.' + file_format)

    ffmpeg.run(stream)


@app.route('/pexeso', methods=['GET'])
def showPexeso():
    return template('pexeso.tpl')


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
    app.run(host='0.0.0.0', debug=False)
