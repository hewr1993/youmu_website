__author__ = 'badpoet'

from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort)

from flask.ext.login import (login_required, current_user, login_user, logout_user, confirm_login)
from .service import VideoService

import json
import os
import mimetypes
from werkzeug.utils import secure_filename
from tempfile import mktemp

video = Blueprint("video", __name__, url_prefix = "/api/video")


@video.route("/", methods = ["GET"])
def get_video_list():
    videos = VideoService.get_video_list()
    videos = [video.to_dict() for video in videos]
    return json.dumps(videos, ensure_ascii = False)


@video.route("/<video_id>", methods = ["GET"])
def get_video_by_id(video_id):
    v = VideoService.get_video_by_id(video_id)
    if v:
        if v.valid(current_user.id):
            v = v.to_dict()
        else:
            v = None
    return json.dumps(v, ensure_ascii = False)


@video.route("/<video_id>/_play", methods = ["POST"])
def add_play_count(video_id):
    VideoService.add_play_count(video_id)
    return ""


@video.route("/<video_id>/_like", methods = ["GET", "POST"])
def like(video_id):
    if request.method == "GET":
        data = { "total": VideoService.count_like_info_by_video(video_id) }
        return json.dumps(data, ensure_ascii = False)
    if request.method == "POST":
        if not current_user.is_anonymous():
            VideoService.click_like(current_user.id, video_id)
        return is_liked_by_me(video_id)


@video.route("/<video_id>/_like/<user_id>", methods = ["GET"])
def is_liked_by_user(video_id, user_id):
    state = VideoService.has_liked(user_id, video_id)
    return json.dumps({ "like": "yes" if state else "no" }, ensure_ascii = False)


@video.route("/<video_id>/_like/_me", methods = ["GET"])
def is_liked_by_me(video_id):
    if current_user.is_anonymous():
        return '{"like": "no"}'
    state = VideoService.has_liked(current_user.id, video_id)
    return json.dumps({ "like": "yes" if state else "no" }, ensure_ascii = False)


@video.route("/upload", methods = ["POST"])
def upload_video():
    if current_user.is_anonymous():
        return '{"state":"fail"}'
    UPLOAD_FOLDER = "youmu/static/uploads/videos/"
    ALLOWED_MIMETYPES = ("video/mp4", "image/png")
    f = request.files['file']
    fname = mktemp(suffix='_', prefix='u', dir=UPLOAD_FOLDER) + secure_filename(f.filename)
    f.save(fname)
    if mimetypes.guess_type(fname)[0] not in ALLOWED_MIMETYPES:
        os.remove(fname)
        return json.dumps({"state":"fail", "content":"wrong mime type"}, ensure_ascii = False)
    postBody = json.loads(request.data)
    obj = Video(owner_id = current_user.id,
        title = postBody["title"],
        upload_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),
        cover = "",
        description = postBody["description"])
    VideoService.insert_video(obj, fname)
    return json.dumps({"state":"success"}, ensure_ascii = False)
