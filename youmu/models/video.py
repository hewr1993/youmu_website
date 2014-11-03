__author__ = 'badpoet'

import json

class Video(object):

    def __init__(self, video_id = "", title = "", cover = "", description = "",
                 play_count = 0, like = 0, owner_id = "", disabled = False,
                 upload_time = "", length = 0, tags = ()):
        self.video_id = unicode(video_id)
        self.title = title
        self.cover = cover
        self.description = description
        self.play_count = int(play_count)
        self.like = int(like),
        self.owner_id = owner_id,
        self.disabled = disabled,
        self.upload_time = upload_time,
        self.length = int(length),
        self.tags = tags

    def to_dict(self):
        dic = {
            "video_id": self.video_id,
            "title": self.title,
            "cover": self.cover,
            "description": self.description,
            "play_count": self.play_count,
            "like": self.like,
            "owner_id": self.owner_id,
            "disabled": self.disabled,
            "upload_time": self.upload_time,
            "length": self.length,
            "tags": self.tags
        }
        return dic

