#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date, timedelta
import math
import os

from werkzeug.utils import secure_filename

from flask import Blueprint
from flask import request, redirect, url_for

from flask import render_template as template
from flask import current_app as application


from app.finance.forms import InterestRateForm, DocumentUploadForm


finance_blueprint = Blueprint('finance', __name__)

INTEREST_RATES = {
    "2016":
        {
            "0": 0.01,
            "1": 0.012
        },

    "2017":
        {
            "0": 0.02,
            "1": 0.022
        },

    "2018":
        {
            "0": 0.03,
            "1": 0.032
        },

    "2019":
        {
            "0": 0.03,
            "1": 0.032
        }

}


# MAIN
@finance_blueprint.route('/uroky', methods=['GET', 'POST'])
def show_interest():
    form = InterestRateForm(request.form)
    if request.method == 'GET':
        return template('finance/interest.html.j2', form=form)
    elif request.method == "POST":
        if not form.validate_on_submit():
            return template('finance/interest.html.j2', form=form)
        # calculate interest
        amount = form.amount.data
        date_from = form.date_from.data
        date_to = form.date_to.data
        interest = 0

        log = []

        # print("Starting - from {} to {}.".format(date_from, date_to))

        is_last = False
        while (date_from != date_to):
            # TODO - správně datediff
            new_date_from = min(round_date_to_next_nearest_halfyear(date_from), date_to)
            if new_date_from == date_to:
                is_last = True
            date_diff = abs(date_from - new_date_from).days + 1
            interest_rate = INTEREST_RATES[str(date_from.year)][str(math.floor(date_from.month / 6.1))]
            interest += date_diff * interest_rate * (amount / 365)
            log.append("Added interest: from {} to {} ({} days), interest rate {}, total {}".format(date_from, new_date_from, date_diff, interest_rate, interest))
            # print("Added interest: From {} to {}, interest rate {}, total {}".format(date_from, new_date_from, interest_rate, interest))
            date_from = new_date_from
            if not is_last:
                date_from = date_from + timedelta(days=1)

        return template('finance/interest.html.j2', form=form, log=log)


def round_date_to_next_nearest_halfyear(old_date):
    if old_date.month <= 6:
        new_date = date(old_date.year, 6, 30)
    else:
        new_date = date(old_date.year, 12, 31)

    return new_date


@finance_blueprint.route('/uploaddoc', methods=['GET', 'POST'])
def show_upload():
    from werkzeug.datastructures import CombinedMultiDict
    form = DocumentUploadForm(CombinedMultiDict((request.files, request.form)))
    # form = DocumentUploadForm(CombinedMultiDict((request.files, request.form)))
    if request.method == 'GET':
        return template('finance/file_upload.html.j2', form=form)
    elif request.method == "POST":
        if not form.validate_on_submit():
            return template('finance/file_upload.html.j2', form=form)

        file = form.document_file.data
        if file.filename == '':
            application.logger.warning('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)

            file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))

            # return redirect(url_for('uploaded_file', filename=file.filename))
            return redirect(request.url)
