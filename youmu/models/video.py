__author__ = 'badpoet'

import json

class Video(object):

    def __init__(self, video_id = "", title = "", cover = "", description = "", play_count = "0"):
        self.video_id = video_id
        self.title = title
        self.cover = cover
        self.description = description
        self.play_count = int(play_count)

    def to_dict(self):
        dic = {
            "video_id": self.video_id,
            "title": self.title,
            "cover": self.cover,
            "description": self.description,
            "play_count": self.play_count
        }
        return dic

    def __repr__(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def fromMongo(db_object):
        res = Video()
        # set attributes, etc
        return res
