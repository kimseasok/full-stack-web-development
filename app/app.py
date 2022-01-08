from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

def app_factory(app, config=None, with_db=False):

    current_app = app.config.from_object(config) if config else app

    db = SQLAlchemy(app=current_app)

    return app, db