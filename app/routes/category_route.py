from flask import Blueprint, make_response

category_route = Blueprint("category_route", __name__, url_prefix="/category")


@category_route.route("/", methods=["GET"])
def category_view():
    return make_response({"categories": ["web development", "soft engineering"]})
