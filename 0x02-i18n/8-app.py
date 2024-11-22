#!/usr/bin/env python3
"""Basic flask server with i18n"""

from datetime import datetime

from flask import Flask, g, render_template, request
from flask_babel import Babel, format_datetime
from pytz import UnknownTimeZoneError, timezone


class Config(object):
    """Flask application configs"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
# babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Gets the current user from url params"""
    user_id = request.args.get("login_as", type=int)
    if user_id:
        return users.get(user_id)


@app.before_request
def before_request():
    """Sets the current user for a request in a global object"""
    user = get_user()
    if user:
        g.user = user


# @babel.localeselector
def get_locale():
    """Returns a request's locale

    Use the locale specified in the request params or
    try match the best language from the `Accept-Language` header
    against the config languages
    """
    locale = request.args.get("locale")
    if not locale and g.get("user"):
        locale = g.user.get("locale")

    if locale in app.config["LANGUAGES"]:
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


# @babel.timezoneselector
def get_timezone():
    """Returns a request's timezone"""
    t_zone = request.args.get("timezone")
    if not timezone and g.get("user"):
        t_zone = g.user.get("timezone")

    try:
        return timezone(t_zone)
    except UnknownTimeZoneError:
        return timezone("UTC")


babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route("/")
def hello():
    """Returns a hello world page"""

    data = {"time": format_datetime(datetime.now())}
    if g.get("user"):
        data["username"] = g.user["name"]

    return render_template("8-index.html", **data)


if __name__ == "__main__":
    app.run()
