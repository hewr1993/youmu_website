__author__ = 'badpoet'

from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort)

from flask.ext.login import (login_required, current_user, login_user, logout_user, confirm_login)

barrage = Blueprint("barrage", __name__, url_prefix = "/api/barrage")

@barrage.route("/video/<video_id>", method = ["GET"])
def get_video_barrage(video_id):
    pass

@barrage.route("/video/<video_id>", method = ["POST"])
def post_video_barrage(video_id):
    pass
