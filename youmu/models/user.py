__author__ = 'badpoet'

import json
from youmu.api.user.service import UserService

class User(object):

    def __init__(self, id = "", mid = "", name = "", avatar = "", password = ""):
        self.id = id
        self.mid = mid
        self.name = name
        self.avatar = avatar

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def check_password(self):
        return self.password == password

    def is_admin(self):
        return UserService.is_admin(self.id)

    def to_dict(self):
        dic = {
            "id": self.id,
            "name": self.name,
            "avatar": self.avatar,
            "admin": self.is_admin()
        }
        return dic
