import os

from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='9d84299b4fe71a9e00191d358c58e7bb8e5d08782c9f64db37fca8c6cbda25f2',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from DataBase import database_session
    database_session.init_app(app)

    from .users import bp_users
    app.register_blueprint(bp_users)

    return app
