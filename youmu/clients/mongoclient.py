__author__ = 'badpoet'

import pymongo
from bson.objectid import ObjectId

from youmu.config import DefaultConfig

from youmu.models.video import Video

class MongoClient(Object):

    def __init__(self, host = DefaultConfig.MONGO_HOST, port = DefaultConfig.MONGO_PORT):
        self.db = pymongo.Connection(host, port)["youmu"]
        # self.db.authenticate(username, password)
        self.user_col = self.db["user"]
        self.video_col = self.db["video"]

    # ABOUT USER

    def get_user_by_id(self, user_id):
        pass

    def get_user_by_mid(self, user_mongo_id):
        pass

    # ABOUT VIDEO

    def get_video_by_id(self, vid):
        some_query_result = None
        # TODO mongo query
        return Video.fromMongo(some_query_result)
