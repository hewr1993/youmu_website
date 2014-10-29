__author__ = 'badpoet'

import pymongo
from bson.objectid import ObjectId

from youmu.config import DefaultConfig

class MongoClient(Object):

    def __init__(self, host = DefaultConfig.MONGO_HOST, port = DefaultConfig.MONGO_PORT):
        self.db = pymongo.Connection(host, port)["youmu"]
        # self.db.authenticate(username, password)
        self.user_col = self.db["user"]
        self.video_col = self.db["video"]

    # ABOUT USER

    def get_user_by_id(self, user_id):
        return self.user_col.find_one({"id": user_id})

    def get_user_by_mid(self, user_mongo_id):
        return self.user_col.find_one({"_id": ObjectId(user_mongo_id)})

    # ABOUT VIDEO

    '''
    def get_video_by_id(self, vid):
        some_query_result = None
        # TODO mongo query
        return Video.fromMongo(some_query_result)
    '''