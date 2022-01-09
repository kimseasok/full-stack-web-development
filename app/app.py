from flask import Flask
from flask.helpers import make_response
from flask_sqlalchemy import SQLAlchemy

from .database import session

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():

    forum = session.query(Forum).filter(Forum.id == 10).one_or_none()

    # new_forum = Forum("test forum 2", "what the description")
    # session.add(new_forum)
    # session.commit()

    return make_response("Hello World", 200)

def app_factory(app, config=None, with_db=False):

    current_app = app.config.from_object(config) if config else app

    # db = SQLAlchemy(app=current_app)

    return app