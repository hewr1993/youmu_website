__author__ = 'badpoet'

from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort)

from flask.ext.login import (login_required, current_user, login_user, logout_user, confirm_login)
from .service import CommentService

import json

comment = Blueprint("comment", __name__, url_prefix = "/api/comment")

@comment.route("/video/<video_id>", method = ["GET", "POST"])
def work_on_video(video_id):
    if request.method == "GET":
        comments = CommentService.get_comments_by_video_id(video_id)
        return json.dumps(comments, ensure_ascii = False)
    else:
        if not current_user.id:
            return '{ "state": "no" }'
        body = json.loads(request.data)
        content = body.get("content", "")
        if not content:
            return '{ "state": "no" }'
        CommentService.comment_on(current_user.id, video_id, content, "")
        return '{ "state": "yes" }'

@comment.route("/user/<user_id>", method = ["GET"])
def work_on_user(user_id):
    comments = CommentService.get_comments_by_user_id(user_id)
    return json.dumps(comments, ensure_ascii = False)
