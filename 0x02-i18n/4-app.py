#!/usr/bin/env python3
""" Get locale from request"""

from flask import Flask, render_template, request
from typing import Any
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """class with local"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """getting local"""
    if 'locale' in request.args:
        req_locale = request.args.get('locale')
        if req_locale in app.config['LANGUAGES']:
            return req_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Get locale from request"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
