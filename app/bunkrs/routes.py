#!/usr/bin/env python
# -*- coding: utf-8 -*-
# run by pyserver

import os
from flask import Blueprint
from flask import redirect

from flask import render_template as template

from app.bunkrs import models

from app.bunkrs import get_bunkrs

BLUEPRINT_ROOT = os.path.dirname(os.path.realpath(__file__))

bunkrs_blueprint = Blueprint('bunkrs', __name__)


@bunkrs_blueprint.route('/bunkrs', methods=['GET'])
@bunkrs_blueprint.route('/bunkrs/<type>', methods=['GET'])
def showBunkrs(type=None):
    if type == "sale":
        bunkrs = models.Bunkr.loadSale()
    elif type == "prepare":
        bunkrs = models.Bunkr.loadPrepare()
    else:
        bunkrs = models.Bunkr.loadAll()

    return template('bunkrs/bunkrs.tpl', bunkrs=bunkrs)


@bunkrs_blueprint.route('/get_bunkrs', methods=['GET'])
def getBunkrs():
    get_bunkrs.main()
    return redirect('/bunkrs')
