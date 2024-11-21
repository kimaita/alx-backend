#!/usr/bin/env python3
"""Basic flask server with i18n"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Flask application configs"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Try match the best language from the `user accept` header
    the browser transmits against the config languages
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def hello():
    """Returns a hello world page"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
