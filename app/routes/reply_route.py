from flask import Blueprint, render_template, make_response, abort, request, redirect, url_for

from app.database import session
from app.models import ForumModel, ReplyModel
from app.utits.validators import ReplyForm

reply_route = Blueprint("reply_route", __name__, url_prefix="/reply")

@reply_route.route("/update/<reply_id>", methods=["GET", "POST"])
def update_reply(reply_id):


    if request.method == "POST":
        form_data = ReplyForm(request.form)

        if not form_data.validate():
            abort(400)
            
    form_dict = {}

    form_dict = request.form.to_dict()

    current_reply = session.query(ReplyModel).filter(ReplyModel.id == reply_id).one_or_none()

    if form_dict:
        for key, value in form_dict.items():
            if hasattr(current_reply, key) and getattr(current_reply, key) != value:
                setattr(current_reply, key, value)
        session.commit()

        redirect_url = f"{url_for('static_route.home')}{current_reply.forum.slush}"

        return redirect(redirect_url)


    if not current_reply:
        abort(404)

    forum = session.query(ForumModel).filter(ForumModel.slush == current_reply.forum.slush).one_or_none()

    replies = session.query(ReplyModel).filter(ReplyModel.forum_id == forum.id).all()

    return render_template("single-forum.html", title=forum.title, forum=forum, replies=replies, reply=current_reply)


@reply_route.route("/delete/<reply_id>", methods=["POST"])
def delete_reply(reply_id):
    reply = session.query(ReplyModel).filter(ReplyModel.id == reply_id).one_or_none()

    if not reply:
        abort(500)

    redirect_url = f"{url_for('static_route.home')}{reply.forum.slush}"

    session.delete(reply)
    session.commit()

    return redirect(redirect_url)