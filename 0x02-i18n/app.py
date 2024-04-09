#!/usr/bin/python3

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import datetime


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """getting user"""
    return users.get(int(user_id))


@app.before_request
def before_request():
    """before locale"""
    user_id = request.args.get('login_as')
    g.user = get_user(user_id)


@babel.localeselector
def get_locale() -> dict:
    """getting locale"""
    if g.user:
        return g.user['locale']
    return request.accept_languages.best_match(['en', 'fr'])


@app.route('/')
def index() -> str:
    """returning template"""
    current_time = datetime.datetime.now(datetime.timezone.utc)
    if g.user and 'timezone' in g.user:
        user_timezone = datetime.timezone(
            datetime.timedelta(hours=3))  # Use g.user['timezone'] instead
        current_time = current_time.astimezone(user_timezone)
    formatted_time = current_time.strftime(
        '%b %d, %Y, %I:%M:%S %p')  # Change format as needed
    return render_template('index.html', current_time=formatted_time)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
