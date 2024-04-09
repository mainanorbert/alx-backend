#!/usr/bin/env python3
'''setting up babel'''

from flask import Flask, render_template
from flask_babel import Babel
from typing import Any


class Config:
    LANGUAGES = ['en', 'fr']


app = Flask('__name__')
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> Any:
    '''defining locale'''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
