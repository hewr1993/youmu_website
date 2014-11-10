__author__ = 'badpoet'

import json
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

@user.route("/_transform", methods = ["GET"])
def transform():
    if current_user.is_anonymous():
        return
    UserService.transform_admin(current_user.id)

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
    if current_user.is_anonymous():
        return ""
    return json.dumps(current_user.to_dict(), ensure_ascii = False)

@user.route("/_me", methods = ["PUT"])
def update_me():
    body = json.loads(request.data)
    name = body.get("name", "")
    avatar = body.get("avatar", "")
    msg = UserService.update(current_user.id, name, avatar)
    return json.dumps({ "state": msg })