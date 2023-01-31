#!/usr/bin/env python3
"""Mock logging in"""

from typing import Union
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """Babel configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    """Get user from session as per variable"""
    try:
        login_as = request.args.get('login_as', None)
        user = users[int(login_as)]
    except Exception:
        user = None


@app.before_request
def before_request():
    """OPerations b4 requests"""
    user = get_user()
    g.user = user


@app.route("/", methods=['GET'], strict_slashes=False)
def index() -> str:
    """render template for Babel usage"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """determine the best match with supported lang."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
