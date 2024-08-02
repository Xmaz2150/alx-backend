#!/usr/bin/env python3
"""
internationaliztion module
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Babel configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    determines the best match with our supported languages
    """
    return request.accept_languages.best_match(
            app.config['BABEL_DEFAULT_TIMEZONE'])


@app.route('/', strict_slashes=False)
def index():
    """
    main route
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
