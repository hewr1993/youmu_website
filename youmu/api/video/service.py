#!/usr/bin/env python

"""Backend video management module.
"""

from youmu.clients import mongo
from youmu.models.video import Video

__author__ = 'badpoet'

class VideoService(object):

    @staticmethod
    def mto(item):
        return Video(
            video_id = item.get("video_id"),
            title = item.get("title", "Untitled Video"),
            owner_id = item.get("owner_id", ""),
            disabled = item.get("disabled", False),
            upload_time = item.get("upload_time", "1900-01-01-00:00:00"),
            length = item.get("length", 0),
            tags = item.get("tags", []),
            cover = item.get("cover", ""),
            description = item.get("description", "You know nothing, Jon Snow."),
            play_count = item.get("play_count", 0),
            like = item.get("like", 0)
        )

    @staticmethod
    def insert_video(video):
        video.video_id = mongo.assign_video_id()

    @staticmethod
    def get_video_list():
        res = mongo.get_video_list()
        if res is None:
            return None
        videos = [VideoService.mto(item) for item in res]
        return videos

    @staticmethod
    def get_video_by_id(video_id):
        item = mongo.get_video_by_id(video_id)
        if item is None:
            return None
        return VideoService.mto(item)

    @staticmethod
    def add_play_count(id):
        mongo.add_video_play_count(id)

    @staticmethod
    def has_liked(user_id, video_id):
        if not user_id:
            return False
        return mongo.query_like_info(user_id, video_id)

    @staticmethod
    def click_like(user_id, video_id):
        if mongo.query_like_info(user_id, video_id):
            mongo.delete_like_info(user_id, video_id)
        else:
            mongo.create_like_info(user_id, video_id)

    @staticmethod
    def count_like_info_by_video(video_id):
        return mongo.count_like_info_by_video(video_id)
