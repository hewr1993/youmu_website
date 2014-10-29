__author__ = 'badpoet'

from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort)

from .service import UserService

user = Blueprint("user", __name__, url_prefix = "/api/user")

