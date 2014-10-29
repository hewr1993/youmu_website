__author__ = 'badpoet'

import json

class User(object):

    def __init__(self, id = "", mid = "", name = "", avatar = "", password = ""):
        self.id = id
        self.mid = mid
        self.name = name
        self.avatar = avatar
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def check_password(self, password):
        return self.password == password

    def to_json(self):
        dic = {
            "id": self.id,
            "name": self.name,
            "avatar": self.avatar
        }
        return json.dumps(dic, ensure_ascii = False)
