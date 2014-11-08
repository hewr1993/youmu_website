__author__ = 'badpoet'

from youmu.models.comment import Comment
from youmu.clients import mongo
from datetime import datetime

class CommentService(object):

    @staticmethod
    def mto(item):
        print item
        return Comment(
            item.get("comment_id"),
            item.get("user_id"),
            item.get("video_id"),
            item.get("content"),
            item.get("reply_to"),
            item.get("reply_time"),
            int(item.get("floor"))
        )

    @staticmethod
    def comment_on(user_id, video_id, content, reply_to = ""):
        floor = mongo.assign_comment_floor(video_id)
        mongo.insert_comment({
            "comment_id": video_id + ":" + str(floor),
            "user_id": user_id,
            "video_id": video_id,
            "content": content,
            "floor": floor,
            "reply_to": reply_to,
            "reply_time": datetime.now()
        })

    @staticmethod
    def get_comments_by_video_id(video_id):
        return [CommentService.mto(item) for item in mongo.get_comment_by_video_id(video_id)]

    @staticmethod
    def get_comments_by_user_id(user_id):
        return [CommentService.mto(item) for item in mongo.get_comment_by_user_id(user_id)]