__author__ = 'badpoet'

from youmu.clients import mongo
from youmu.models.user import User

class UserService(object):

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
        return self.load_by_id(id)
