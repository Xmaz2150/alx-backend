#!/usr/bin/env python3
"""
internationaliztion module
"""
internationaliztion module
    main route
    Babel configuration class
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
    if request.args.get('locale'):
        lang = request.args.get('locale')
        if lang in app.config['LANGUAGES']:
            return lang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def index():
    """
    main route
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
