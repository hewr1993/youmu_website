__author__ = 'badpoet'

from youmu.clients import mongo
from youmu.models.video import Video

class VideoService(object):

    @staticmethod
    def get_video_list():
        res = mongo.get_video_list()
        if res is None:
            return None
        videos = []
        for item in res:
            videos.append(Video(
                video_id = item.get("video_id"),
                title = item.get("title"),
                cover = item.get("cover"),
                description = item.get("description"),
                play_count = item.get("play_count")
            ))
        return videos
