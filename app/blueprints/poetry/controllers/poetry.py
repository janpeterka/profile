import os

from flask import Blueprint
from flask import redirect, url_for, request
from flask import render_template as template

from app.helpers.form import save_form_to_session, create_form

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
    form = create_form(PoetryForm)
    return template("poetry/new.html.j2", form=form)


@poetry_blueprint.route("/poetry/show/<id>", methods=["GET"])
def show(id):
    item = Poetry.load(id)

    return template("poetry/show.html.j2", poetry=item)


@poetry_blueprint.route("/poetry/post", methods=["POST"])
def post():
    form = PoetryForm(request.form)
    if not form.validate_on_submit():
        save_form_to_session(request.form)
        return redirect(url_for("DietsView:new"))

    # save photo
    #
    #
    poetry = Poetry(
        name=request.form.get("name"),
        created_by=request.form.get("created_by"),
        latitude=request.form.get("latitude"),
        longitude=request.form.get("longitude"),
        # photo_path=
    )
    poetry.save()
    return redirect("show/" + str(poetry.id))
