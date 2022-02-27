from flask import Flask, Blueprint

from app.routes import *

app = Flask(__name__)

all_routes = [route for name, route in globals().items() if isinstance(route, Blueprint)]

for route in all_routes:
    app.register_blueprint(route)


def app_factory(app, config=None, with_db=False):

    current_app = app.config.from_object(config) if config else app

    # db = SQLAlchemy(app=current_app)

    return app