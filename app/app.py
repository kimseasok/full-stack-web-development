from flask import Flask

from .routes import user_route

app = Flask(__name__)


app.register_blueprint(user_route)

def app_factory(app, config=None, with_db=False):

    current_app = app.config.from_object(config) if config else app

    # db = SQLAlchemy(app=current_app)

    return app