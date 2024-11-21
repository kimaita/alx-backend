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
    """Returns a request's locale
    
    Use the locale specified in the request params or    
    try match the best language from the `Accept-Language` header
    against the config languages
    """
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def hello():
    """Returns a hello world page"""
    data = {
        "home_title": "Welcome to Holberton",
        "home_header": "Hello world",
    }
    return render_template("3-index.html", **data)


if __name__ == "__main__":
    app.run()
