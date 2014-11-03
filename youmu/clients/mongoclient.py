__author__ = 'badpoet'

import pymongo
from bson.objectid import ObjectId

from youmu.config import DefaultConfig

class MongoClient(object):

    def __init__(self, host = DefaultConfig.MONGO_HOST, port = DefaultConfig.MONGO_PORT):
        self.db = pymongo.Connection(host, port)["youmu"]
        # self.db.authenticate(username, password)
        self.user_col = self.db["user"]
        self.video_col = self.db["video"]

    # ABOUT USER

    def has_user_id(self, user_id):
        return self.user_col.find_one({"id": user_id}) is not None

    def get_user_by_id(self, user_id):
        return self.user_col.find_one({"id": user_id})

    def get_user_by_mid(self, user_mongo_id):
        return self.user_col.find_one({"_id": ObjectId(user_mongo_id)})

    def insert_user(self, user_dict):
        self.user_col.insert(user_dict)

    # ABOUT VIDEO

    def get_video_by_id(self, video_id):
        return self.video_col.find_one({"id": video_id})

    def get_video_list(self, offset = 0, size = 10):
        cursor = self.video_col.find()[offset : size]
