import os

from werkzeug.datastructures import CombinedMultiDict

from flask import Blueprint
from flask import redirect, request, send_from_directory
from flask import render_template as template

from app.helpers.form import save_form_to_session, create_form
from app.handlers.files import FileHandler

from .forms.poetry import PoetryForm

from app.blueprints.poetry.models.poetry import Poetry


BLUEPRINT_ROOT = os.path.dirname(os.path.realpath(__file__))

poetry_blueprint = Blueprint("poetry", __name__)


@poetry_blueprint.route("/poetry", methods=["GET"])
@poetry_blueprint.route("/poetry/", methods=["GET"])
@poetry_blueprint.route("/poetry/all", methods=["GET"])
def index():
    all_poetry = Poetry.load_all()
    return template("poetry/index.html.j2", all_poetry=all_poetry)


@poetry_blueprint.route("/poetry/new", methods=["GET"])
def new():
    form = PoetryForm(CombinedMultiDict((request.files, request.form)))
    return template("poetry/new.html.j2", form=form)


@poetry_blueprint.route("/poetry/show/<id>", methods=["GET"])
def show(id):
    item = Poetry.load(id)
    item.file_path = FileHandler().get_path(item)

    return template("poetry/show.html.j2", poetry=item)


@poetry_blueprint.route("/poetry/post", methods=["POST"])
def post():
    form = PoetryForm(CombinedMultiDict((request.files, request.form)))
    if not form.validate_on_submit():
        save_form_to_session(request.form)
        return redirect("/poetry/new")

    secure_filename = FileHandler().save(form.photo.data)

    poetry = Poetry(
        name=form.name.data,
        created_by=form.created_by.data,
        latitude=form.latitude.data,
        longitude=form.longitude.data,
        filename=secure_filename,
    )
    poetry.save()
    return redirect("show/" + str(poetry.id))


@poetry_blueprint.route("/poetry/images/<item_id>", methods=["GET"])
def images(item_id):
    # from werkzeug.utils import secure_filename
    item = Poetry.load(item_id)
    print(item.filename)
    # path = os.path.join("/home/jan/programming/profile/app/uploads/images/")
    # path = os.path.join(BLUEPRINT_ROOT, "../../../uploads/images/")
    # print(path)
    # return send_from_directory(path, secure_filename(item.filename))

    file = FileHandler().show(item)
    print(file)
    return file
