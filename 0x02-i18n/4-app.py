#!/usr/bin/env python3
"""Basic flask app."""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """ list des langues prises en charges"""
    LANGUAGES = ['en', 'fr']
    # default config
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


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
