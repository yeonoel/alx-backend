#!/usr/bin/env python3
"""Basic flask app."""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(Object):
    """ list des langues prises en charges"""
    LANGUAGES = ["en", "fr"]
    # default config
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """ return template """
    return render_template('index.html')


if '__name__' == '__main__':
    app.run()
