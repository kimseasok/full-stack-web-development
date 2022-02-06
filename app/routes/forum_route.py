from flask import Blueprint, make_response

forum_route = Blueprint("forum_route", __name__, url_prefix="/forum")


@forum_route.route("/tag", methods=["GET"])
def tag_create():

    return make_response({"message": "created"}, 201)
