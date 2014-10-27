__author__ = 'badpoet'

from youmu.clients.mongoclient import MongoClient

mongo = MongoClient()

class VideoService(object):

    @staticmethod
    def get_video_by_id(vid):
        return mongo.get_video_by_id(vid)

