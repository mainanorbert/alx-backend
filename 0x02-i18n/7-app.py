from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    return users.get(int(user_id))

@app.before_request
def before_request():
    user_id = request.args.get('login_as')
    g.user = get_user(user_id)

@babel.localeselector
def get_locale():
    if g.user:
        return g.user['locale']
    return request.accept_languages.best_match(['en', 'fr'])

@babel.timezoneselector
def get_timezone():
    user_timezone = request.args.get('timezone')
    if user_timezone:
        try:
            pytz.timezone(user_timezone)
            return user_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user and 'timezone' in g.user:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return 'UTC'

@app.route('/')
def index():
    return render_template('7-index.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
