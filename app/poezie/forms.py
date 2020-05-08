from wtforms import StringField, SubmitField
from wtforms import validators

from flask_wtf import FlaskForm
from flask_wtf.file import FileField

from wtforms import FloatField


class ComaFloatField(FloatField):
    def process_formdata(self, valuelist):
        if valuelist:
            try:
                self.data = float(valuelist[0].replace(",", "."))
            except ValueError:
                self.data = None
                raise ValueError(self.gettext("Toto není desetinné číslo"))


class PoezieForm(FlaskForm):
    name = StringField("Báseň", [validators.InputRequired("Musí být vyplněno")])
    created_by = StringField("Umístil", [validators.InputRequired("Musí být vyplněno")])

    latitude = ComaFloatField("X", [validators.InputRequired("Musí být vyplněno")])
    longitude = ComaFloatField("Y", [validators.InputRequired("Musí být vyplněno")])

    photo = FileField("Fotka")
    submit = SubmitField("Nahrát nový příspěvek")
