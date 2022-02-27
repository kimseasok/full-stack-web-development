from flask import Blueprint, render_template, make_response, abort, request, redirect, url_for

from app.database import session
from app.models import ForumModel, ReplyModel

static_route = Blueprint("static_route", __name__)

@static_route.route("/", methods=["GET"])
def home():

    forums = session.query(ForumModel).all()

    return render_template("index.html", title="Home", forums=forums)

@static_route.route("/<slush>", methods=["GET"])
def single_forum(slush):

    forum = session.query(ForumModel).filter(ForumModel.slush == slush).one_or_none()

    if not forum:
        abort(404)

    replies = session.query(ReplyModel).filter(ReplyModel.forum_id == forum.id).all()

    return render_template("single-forum.html", title=forum.title, forum=forum, replies=replies)

@static_route.route("/<slush>", methods=["POST"])
def create_reply(slush):
    current_forum = session.query(ForumModel).filter(ForumModel.slush == slush).one_or_none()

    if not current_forum:
        abort(400)

    reply = request.form.to_dict()
    reply.update({"forum_id": current_forum.id})

    new_reply = ReplyModel(reply)
    session.add(new_reply)
    session.commit()

    redirect_url = f"{url_for('static_route.home')}{current_forum.slush}"

    return redirect(redirect_url)

   
@static_route.route("/new", methods=["GET"])
def new_forum():
    forums = [ForumModel({"title": "Web Development", "description": "topics related to web development", "slush": "web-development"})]
    session.add_all(forums)
    session.commit()
    return make_response({"test": "succes"}, 200)

