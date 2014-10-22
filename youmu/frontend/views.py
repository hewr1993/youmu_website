__author__ = 'badpoet'

from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort)

frontend = Blueprint("frontend", __name__)

@frontend.route('/')
def index():
    return render_template('index.html')

@frontend.route('/videos/<video_id>')
def display(video_id):
	return render_template('video.html', video_id = video_id)

