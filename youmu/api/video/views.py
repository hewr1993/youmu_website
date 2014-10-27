__author__ = 'badpoet'

from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort)

from .service import VideoService

video = Blueprint("video", __name__, url_prefix = "/api/video")

@video.route('/video/<vid>', methods = ['GET'])
def get_video_by_id(vid):
    res = VideoService.get_video_by_id(vid)
    if not res:
        return 'fake json'
    else:
        return 'real json'  # eg. res.to_json() (NOT IMPLEMENTED)