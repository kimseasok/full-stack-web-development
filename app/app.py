from flask import Flask
from flask.helpers import make_response
from sqlalchemy import desc, asc

from .database import session
from .models import *

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():

    # new_forum = ForumModel("General IT Topics", "General topics related to IT")

    # session.add(new_forum)

    # session.commit()

    # forum = session.query(ForumModel).filter_by(id=2).one()

    # forum.title = "Software development"
    # forum.descrciption = "Any topic related software developement"

    # session.commit()

    # delete_forum = session.query(ForumModel).filter(ForumModel.id == 3).delete()
    # session.commit()

    # print(delete_forum, "============delete id")

    # question = ReplyModel(
    #     "How to connect to db using sqlalchemy",
    #     "I'm trying to connect db using creating, but no luck. anyone please help", 
    #     2
    # )

    # question1 = ReplyModel("How to create route in Flask framework?", "whatever", 1)

    # session.add_all([question, question1])

    # session.commit()

    forum2 = session.query(ForumModel).filter(ForumModel.id == 2).one()

    reply1 = session.query(ReplyModel).filter(ReplyModel.id == 1).one()

    print(reply1.forum.title)

    # print(forum2.replies[0].title)


    return make_response("Hello World", 200)

def app_factory(app, config=None, with_db=False):

    current_app = app.config.from_object(config) if config else app

    # db = SQLAlchemy(app=current_app)

    return app