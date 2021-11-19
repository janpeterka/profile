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
    return template("main/dashboard.html.j2")


@main_blueprint.route("/newsletter", methods=["GET"])
def show_newsletter():
    return template("main/newsletter_subscribe.html.j2")


@main_blueprint.route("/portfolio", methods=["GET"])
def show_portfolio():
    return template("main/portfolio.html.j2")


@main_blueprint.route("/songbooks", methods=["GET"])
@main_blueprint.route("/zpevniky", methods=["GET"])
def show_songbooks():
    folders = [
        Folder(folder[0])
        for folder in os.walk(SONGBOOKS_DIR)
        if os.path.isdir(folder[0])
    ]

    if folders:
        del folders[0]

    for folder in folders:
        folder.name = Path(folder.path).name

    folders.sort(key=lambda x: x.name, reverse=False)

    return template("main/songbooks.html.j2", folders=folders)


@main_blueprint.route("/songbooks/<filename>", methods=["GET"])
def download_songbook_file(filename):
    return send_file(
        SONGBOOKS_DIR + filename.split(".")[0] + "/" + filename,
        attachment_filename=filename,
    )


@main_blueprint.route("/studentske_projekty", methods=["GET"])
def show_student_projects():
    return template("main/student_projects.html.j2")


@main_blueprint.route("/better", methods=["GET"])
def show_better_life():
    import datetime
    from ..better_life_tasks import tasks
    from ..better_life_tasks import predictions
    date_as_int = int(datetime.date.today().strftime('%Y%m%d'))
    today_task = tasks[date_as_int % len(tasks)]
    today_prediction = predictions[date_as_int % len(predictions)]
    return template("main/better_life.html.j2", today_task=today_task, today_prediction=today_prediction)
