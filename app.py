#!/usr/bin/env python
# -*- coding: utf-8 -*-

# run by pyserver

from flask import Flask, render_template as template
# from flask import request, redirect
# from flask import flash

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return template('dashboard.tpl')


@app.route('/songbooks', methods=['GET'])
def showSongbooks():
    return template('songbooks.tpl')


@app.route('/portfolio', methods=['GET'])
def showPortfolio():
    return template('portfolio.tpl')


# ERROR
@app.errorhandler(404)
def error404(error):
    return 'Tady nic není (Err404)'


@app.errorhandler(500)
def error500(error):
    return 'Někde se stala chyba (Err500)'


if __name__ == "__main__":
    # app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)
    app.run(debug=True)
