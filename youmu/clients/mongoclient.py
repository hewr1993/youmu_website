__author__ = 'badpoet'

import pymongo
from bson.objectid import ObjectId

from youmu.models.video import Video

class MongoClient(Object):

    def __init__(self):
        # TODO mongo initialization -> ZXK
        pass

    def get_video_by_id(self, vid):
        some_query_result = None
        # TODO mongo query
        return Video.fromMongo(some_query_result)

    def delete_video_by_id(self, vid):
        some_query_result = None
        # TODO mongo query
        return some_query_result
