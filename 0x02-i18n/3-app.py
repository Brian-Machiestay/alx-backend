#!/usr/bin/env python3
""" a simple flask application to demonstrate different languages support"""
from flask import Flask, render_template
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config:
    """configure available languages in this application"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale():
    """get the user's locale"""
    return request.accept_languages.best_match(["en", "fr"])


@app.route('/')
def root():
    """return the root of this application"""
    return(render_template('3-index.html'))


if __name__ == '__main__':
    app.config.from_object(Config)
    app.run(host='0.0.0.0')
