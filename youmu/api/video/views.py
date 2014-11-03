__author__ = 'badpoet'

from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort)

from .service import VideoService

import json

video = Blueprint("video", __name__, url_prefix = "/api/video")

@video.route("/", methods = ["GET"])
def get_video_list():
    videos = VideoService.get_video_list()
    videos = [video.to_dict() for video in videos]
    return json.dumps(videos, ensure_ascii = False)


@video.route("/{id}", methods = ["GET", "POST"])
def get_video_by_id(video_id):
    v = VideoService.get_video_by_id(video_id).to_dict()
    return json.dumps(v, ensure_ascii = False)


@video.route("/{id}", methods = ["POST"])
def add_play_count(video_id):
    VideoService.add_play_count(video_id)