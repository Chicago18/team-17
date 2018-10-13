import os

from flask import Flask
from flask import send_from_directory, abort
import flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Index page
    @app.route('/')
    def index():
        return flask.redirect(flask.url_for('login'))

    # Sign up page
    @app.route('/signup/')
    def signup():
        return flask.render_template("/signup.html")

    # Login page
    @app.route('/login/')
    def login():
        return flask.render_template("/login.html")

    return app