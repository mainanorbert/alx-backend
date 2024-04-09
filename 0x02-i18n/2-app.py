#!/usr/bin/env python3
""" Get locale from request"""

from flask import Flask, render_template, request
from typing import Any
from flask_babel import Babel
from werkzeug.utils import cached_property


app = Flask(__name__)
babel = Babel(app)


class Config:
    """class with local"""
    LANGUAGES = ['en', 'fr']


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """getting local"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Get locale from request"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
