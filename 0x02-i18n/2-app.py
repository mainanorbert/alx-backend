#!/usr/bin/env python3
""" Get locale from request"""

from flask import Flask, render_template, request
from typing import Any
from flask_babel import Babel


app: Flask = Flask(__name__)
babel: Babel = Babel(app)


class Config:
    """class with local"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """getting local"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """Get locale from request"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
