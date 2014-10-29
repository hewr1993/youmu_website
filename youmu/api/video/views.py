__author__ = 'badpoet'

from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort)

from .service import VideoService

import json

video = Blueprint("video", __name__, url_prefix = "/api/video")

@video.route("/", methods = ["GET"])
def get_video_list():
    videos = VideoService.get_video_list()
    videos = [str(video) for video in videos]
    return json.dumps(videos)
