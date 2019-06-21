from flask_wtf import FlaskForm

from wtforms import SubmitField, IntegerField, DateField
from wtforms import validators


class InterestRateForm(FlaskForm):
    amount = IntegerField('Částka', [validators.InputRequired('Částka musí být vyplněna')])
    date_from = DateField('Datum od', [validators.InputRequired('Datum musí být vyplněno')], format='%d.%m.%Y')
    date_to = DateField('Datum do', [validators.InputRequired('Datum musí být vyplněno')], format='%d.%m.%Y')
    submit = SubmitField('Spočítat')