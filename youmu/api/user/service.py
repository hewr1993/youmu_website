__author__ = 'badpoet'

import re

from youmu.clients import mongo
from youmu.models.user import User

class UserService(object):

    @staticmethod
    def is_valid_id(id):
        try:
            id = str(id)
            return re.match(r'[0-9a-zA-Z][0-9a-zA-Z\_]{1,15}', id) != None
        except Exception, e:
            return False

    @staticmethod
    def is_valid_password(password):
        try:
            password = str(password)
            return len(password) >= 6 and len(password) <= 16
        except Exception, e:
            return False

    @staticmethod
    def load_user_by_id(id):
        temp = mongo.get_user_by_id(id)
        if not temp:
            return None
        obj = User(
            id = temp.get("id"),
            mid = str(temp.get("_id")),
            name = temp.get("name"),
            avatar = temp.get("avatar"),
            password = temp.get("password")
        )
        return obj

    @staticmethod
    def create_user(id, name, avatar, password):
        if mongo.has_user_id(id):
            return None
        mongo.insert_user({
            "id": id,
            "name": name,
            "avatar": avatar,
            "password": password
        })
        return UserService.load_by_id(id)

    @staticmethod
    def authenticate(id, password):
        print id, UserService.is_valid_id(id)
        print password, UserService.is_valid_password(password)
        if not UserService.is_valid_id(id) or not UserService.is_valid_password(password):
            return None
        user = UserService.load_user_by_id(id)
        if user is None:
            return None
        else:
            if user.password != password:
                return None
            else:
                return user

