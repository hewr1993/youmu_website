__author__ = 'badpoet'

from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort)
from flask.ext.login import (login_required, current_user, login_user, logout_user, confirm_login)

from .service import UserService
from .forms import LoginForm
import json

user = Blueprint("user", __name__, url_prefix = "/api/user")

# tests begin

@user.route("/_test", methods = ["GET", "POST"])
@login_required
def test():
    return "You're a user!"

@user.route("/_tell", methods = ["GET", "POST"])
def tell():
    if current_user.is_anonymous():
        return "You are a tourist."
    else:
        return "You are " + current_user.name

@user.route("/_login2/<id>/<password>", methods = ["GET"])
def login2(id, password):
    user = UserService.authenticate(id, password)
    if user is not None:
        login_user(user)
        return "success!"
    return "fail!"

# tests end

@user.route("/_login", methods = ["POST"])
def login():
    postBody = json.loads(request.data)
    id = postBody["username"]
    password = postBody["password"]
    user = UserService.authenticate(id, password)
    if user is not None:
        login_user(user)
        return '{"state": "ok"}'
    return '{"state": "failed"}'

@user.route("/_logout", methods = ["POST"])
def logout():
    logout_user()
    return '{"state": "ok"}'

@user.route("/_me", methods = ["GET"])
def me():
    if current_user.is_anonymous:
        return '{"state": "not a user"}'
    return json.dumps(current_user.to_dict(), ensure_ascii = False)
