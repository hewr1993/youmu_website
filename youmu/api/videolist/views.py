__author__ = 'badpoet'

from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort)

from flask.ext.login import (login_required, current_user, login_user, logout_user, confirm_login)
from .service import VideoListService

import json

video_list = Blueprint("videolist", __name__, url_prefix = "/api/videolist")

@video_list.route("/", methods = ["GET"])
def general_query():
    offset = request.args.get('offset', 0)
    size = request.args.get('size', 10)
    order_by = request.args.get('order_by', "upload_time")
    reverse = request.args.get('reverse', 0) > 0
    res = VideoListService.generalGet(offset, size, order_by, reverse)
    res = [v.to_dict() for v in res]
    return json.dumps(res, ensure_ascii = False)