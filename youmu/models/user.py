__author__ = 'badpoet'

from youmu.clients import mongo

class User(object):

    def __init__(self, id = "", mid = "", name = "", avatar = "", password = ""):
        self.id = id
        self.mid = mid
        self.name = name
        self.avatar = avatar
        self.password = password

    @staticmethod
    def fromId(id):
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