__author__ = 'badpoet'

from youmu.models.video import Video
from youmu.api.video.service import VideoService
from youmu.clients import mongo

class VideoListService(object):

    @staticmethod
    def mto(mongo_obj):
        return VideoService.mto(mongo_obj)

    @staticmethod
    def validate_order_by(order_by):
        valid_order_by = ["upload_time", "play_count", "like"]
        if order_by not in valid_order_by:
            order_by = "upload_time"
        return order_by

    @staticmethod
    def general_get(offset = 0, size = 10, order_by = "upload_time", reverse = False, filters = None):
        order_by = VideoListService.validate_order_by(order_by)
        return [VideoListService.mto(item) for item in mongo.get_ordered_video_list({}, offset, size, order_by, reverse)]

    @staticmethod
    def get_with_owner(owner_id, offset = 0, size = 10, order_by = "upload_time", reverse = False, filters = None):
        order_by = VideoListService.validate_order_by(order_by)
        return [VideoListService.mto(item) for item in mongo.get_ordered_video_list(
            { "owner_id": owner_id },
            offset, size, order_by, reverse)]

    @staticmethod
    def query_on_title(title, offset = 0, size = 10, order_by = "upload_time", reverse = False, filters = None):
        order_by = VideoListService.validate_order_by(order_by)
        return [VideoListService.mto(item) for item in mongo.get_ordered_video_list(
            { "title": { "$regex": title } },
            offset, size, order_by, reverse)]
