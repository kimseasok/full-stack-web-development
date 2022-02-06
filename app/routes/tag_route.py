from flask import Blueprint, make_response

from app.models import TagModel
from app.database import session

tag_route = Blueprint("tag_route", __name__, url_prefix="/tag")


@tag_route.route("/", methods=["GET"])
def tag_view():

    tags = [
        TagModel({"name": "Web Development", "description": "whatever"}),
        TagModel({"name": "Soft Engineering", "description": "Whatevery"})
    ]

    print(tags)

    session.add_all(tags)
    session.commit()

    return make_response({"tag": ["angular", "php", "php"]}, 200)
