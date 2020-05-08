from wtforms import StringField, SubmitField
from wtforms import validators

from flask_wtf import FlaskForm
from flask_wtf.file import FileField

from app.helpers.form_fields import ComaFloatField


class PoetryForm(FlaskForm):
    name = StringField("Dílo", [validators.InputRequired("Musí být vyplněno")])
    created_by = StringField("Umístil", [validators.InputRequired("Musí být vyplněno")])

    latitude = ComaFloatField("X", [validators.InputRequired("Musí být vyplněno")])
    longitude = ComaFloatField("Y", [validators.InputRequired("Musí být vyplněno")])

    photo = FileField("Fotka")
    submit = SubmitField("Nahrát nový příspěvek")
