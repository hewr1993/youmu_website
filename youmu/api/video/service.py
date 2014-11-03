#!/usr/bin/env python

"""Backend video management module.
"""

from youmu.clients import mongo
from youmu.models.video import Video

__author__ = 'badpoet'

class VideoService(object):

    @staticmethod
    def get_video_list():
        res = mongo.get_video_list()
        if res is None:
            return None
        videos = [Video(
            video_id = item.get("video_id"),
            title = item.get("title", "Untitled Video"),
            cover = item.get("cover", ""),
            description = item.get("description", "You know nothing, Jon Snow."),
            play_count = item.get("play_count", 0)
        ) for item in res]
        return videos

    @staticmethod
    def get_video_by_id(video_id):
        item = mongo.get_video_by_id(video_id)
        if item is None:
            return None
        return Video(
            video_id = item.get("video_id"),
            title = item.get("title", "Untitled Video"),
            cover = item.get("cover", ""),
            description = item.get("description", "You know nothing, Jon Snow."),
            play_count = item.get("play_count", 0)
        )

    @staticmethod
    def add_play_count(id):
        mongo.add_video_play_count(id)