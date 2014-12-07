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
    def return_query_res(query, offset=0, size=10, order_by="upload_time",
                         reverse=False, show_banned=False, show_disabled=False):
        order_by = VideoListService.validate_order_by(order_by)
        if not show_disabled: query["disabled"] = False
        if not show_banned: query["banned"] = False
        return [VideoListService.mto(item) for item in mongo.get_ordered_video_list(
            query, offset, size, order_by, reverse)]

    @staticmethod
    def general_get(offset = 0, size = 10, order_by = "upload_time", reverse = False,
                    show_banned = False, show_disabled = False):
        return VideoListService.return_query_res({}, offset, size,
                order_by, reverse, show_banned, show_disabled)

    @staticmethod
    def get_with_owner(owner_id, offset=0, size=10, order_by="upload_time",
                       reverse=False, show_banned=False, show_disabled=False):
        query = { "owner_id": owner_id }
        return VideoListService.return_query_res(query, offset, size,
                order_by, reverse, show_banned, show_disabled)

    @staticmethod
    def query_on_title(title, offset=0, size=10, order_by="upload_time",
                       reverse=False, show_banned=False, show_disabled=False):
        query = { "title": { "$regex": title, "$options": "i" } }
        return VideoListService.return_query_res(query, offset, size,
                order_by, reverse, show_banned, show_disabled)
