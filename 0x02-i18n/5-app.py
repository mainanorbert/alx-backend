#!/usr/bin/env python3
'''Mock logging in'''


from flask import Flask, g, render_template, request
from flask_babel import Babel
from typing import Dict


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id: int) -> Dict:
    """function to get user"""
    return users.get(user_id)


@app.before_request
def before_request():
    '''function before request'''
    user_id = request.args.get('login_as')
    g.user = get_user(user_id)


@app.route('/')
def index() -> str:
    '''returns index.html'''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(Debug=True)
