#!/usr/bin/env python3
"""Mock logging in."""

from flask import Flask, render_template, request, g
from flask_babel import Babel,
from typing import Union

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """ list des langues prises en charges"""
    LANGUAGES = ['en', 'fr']
    # default config
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
    """ return a user dictionary or None."""
    try:
        login_as = app.args.get('login_as', None)
        user = users[int(login_as)]
    except Exception:
        user = None


@app.before_request
def before_request():
    """find a user if any, and set it as a global on flask.g.user."""
    user = get_user()
    g.user = user


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ return template """
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    """Get locale from request. """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if '__name__' == '__main__':
    app.run()
