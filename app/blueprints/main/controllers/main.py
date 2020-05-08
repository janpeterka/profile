import os
from pathlib import Path

from flask import Blueprint
from flask import render_template as template
from flask import send_file

from app.blueprints.main.models.folder import Folder


BLUEPRINT_ROOT = os.path.dirname(os.path.realpath(__file__))
SONGBOOKS_DIR = os.path.join(BLUEPRINT_ROOT, "../../../public/songbooks/")

main_blueprint = Blueprint("main", __name__)


# MAIN
@main_blueprint.route("/", methods=["GET"])
def main():
    return template("dashboard.html.j2")


@main_blueprint.route("/newsletter", methods=["GET"])
def show_newsletter():
    return template("newsletter_subscribe.html.j2")


@main_blueprint.route("/portfolio", methods=["GET"])
def show_portfolio():
    return template("portfolio.html.j2")


@main_blueprint.route("/songbooks", methods=["GET"])
@main_blueprint.route("/zpevniky", methods=["GET"])
def show_songbooks():
    folders = []
    for folder in os.walk(SONGBOOKS_DIR):
        if os.path.isdir(folder[0]):
            folders.append(Folder(folder[0]))

    if len(folders) > 0:
        del folders[0]

    for folder in folders:
        folder.name = Path(folder.path).name

    folders.sort(key=lambda x: x.name, reverse=False)

    return template("songbooks.html.j2", folders=folders)


@main_blueprint.route("/songbooks/<filename>", methods=["GET"])
def download_songbook_file(filename):
    return send_file(
        SONGBOOKS_DIR + filename.split(".")[0] + "/" + filename,
        attachment_filename=filename,
    )


@main_blueprint.route("/studentske_projekty", methods=["GET"])
def show_student_projects():
    return template("student_projects.html.j2")
