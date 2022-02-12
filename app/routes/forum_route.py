from flask import Blueprint, make_response, request

from app.database import session
from app.models import ReplyModel, ForumModel, TagModel

forum_route = Blueprint("forum_route", __name__, url_prefix="/forum")


@forum_route.route("/", methods=["GET"])
def tag_create():

    forums = [ForumModel({"title": "Programming", "descrciption": "whatever"})]

    session.add_all(forums)

    session.commit()

    return make_response({"message": "created"}, 201)


@forum_route.route("/reply", methods=["POST"])
def reply_create():

    new_reply = ReplyModel(request.form.to_dict())
    tags = [
        TagModel({"name": "python", "description": "whatever"}),
        TagModel({"name": "flask", "description": "whatever"}),
    ]
    new_reply.tags = tags
    session.add(new_reply)
    session.commit()
    return make_response({"message": "created"}, 201)
