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


PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
SONGBOOKS_DIR = os.path.join(PROJECT_ROOT, 'public/songbooks/')
MMS_DIR = os.path.join(PROJECT_ROOT, 'public/mms/')

main_blueprint = Blueprint('main', __name__)


# MAIN
@main_blueprint.route('/', methods=['GET'])
def main():
    return template('dashboard.tpl')


@main_blueprint.route('/bunkrs', methods=['GET'])
def showBunkrs():
    bunkrs = models.Bunkr.loadAll()
    return template('bunkrs.tpl', bunkrs=bunkrs)


@main_blueprint.route('/songbooks', methods=['GET'])
@main_blueprint.route('/zpevniky', methods=['GET'])
def showSongbooks():
    folders = []
    for folder in os.walk(SONGBOOKS_DIR):
        if os.path.isdir(folder[0]):
            folders.append(models.Folder(folder[0]))

    del folders[0]

    for folder in folders:
        folder.name = Path(folder.path).name

    folders.sort(key=lambda x: x.name, reverse=False)

    return template('songbooks.tpl', folders=folders)


@main_blueprint.route('/songbooks/<name>', methods=['GET'])
def downloadSongbookFile(name):
    return send_file(SONGBOOKS_DIR + name.split('.')[0] + "/" + name, attachment_filename=name)


@main_blueprint.route('/mms2018', methods=['GET'])
@main_blueprint.route('/mms', methods=['GET'])
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


@main_blueprint.route('/mms/<name>', methods=['GET'])
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


@main_blueprint.route('/pexeso', methods=['GET'])
def showPexeso():
    return template('pexeso.tpl')


@main_blueprint.route('/portfolio', methods=['GET'])
def showPortfolio():
    return template('portfolio.tpl')
