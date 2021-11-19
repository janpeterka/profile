# import os
# from pathlib import Path
from flask import render_template as template

from flask import Blueprint

# from flask_security import current_user

auth_blueprint = Blueprint("auth", __name__)


# MAIN
@auth_blueprint.route("/user", methods=["GET"])
def main():
    return template("auth/user.html.j2")
