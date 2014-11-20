__author__ = 'badpoet'

from youmu.clients import mongo

class BarrageService(object):

    @staticmethod
    def add_barrage(barrage):
        # mongo.insert_barrage(barrage.to_dict())
        pass

    @staticmethod
    def get_barrage_on_video(video_id):
        # cursor = mongo.get_barrage_by_video(video_id)
        # res = [BarrageService.mto(e) for e in cursor]
        # return res
        pass
