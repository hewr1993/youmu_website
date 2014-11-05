__author__ = 'badpoet'

from youmu.models.video import Video
from youmu.api.video.service import VideoService
from youmu.clients import mongo

class VideoListService(object):

    @staticmethod
    def mto(mongo_obj):
        return VideoService.mto(mongo_obj)

    @staticmethod
    def generalGet(offset = 0, size = 10, order_by = "upload_time", reverse = False, filters = None):
        valid_order_by = ["upload_time", "play_count", "like"]
        if order_by not in valid_order_by:
            order_by = "upload_time"
        return [VideoListService.mto(item) for item in mongo.get_ordered_video_list(offset, size, order_by, reverse)]
