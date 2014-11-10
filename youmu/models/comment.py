__author__ = 'badpoet'

from youmu.api.user.service import UserService

class Comment(object):

    def __init__(self, comment_id, user_id, video_id, content, reply_to, reply_time, floor = -1):
        self.user_id = user_id
        self.comment_id = comment_id
        self.video_id = video_id
        self.content = content
        self.reply_to = reply_to
        self.reply_time = reply_time
        self.floor = floor

    def to_dict(self):
        user = UserService.load_user_by_id(self.user_id)
        return {
            "comment_id": self.comment_id,
            "user_id": self.user_id,
            "video_id": self.video_id,
            "content": self.content,
            "reply_to": self.reply_to,
            "reply_time": self.reply_time.strftime("%Y-%m-%d-%X"),
            "floor": self.floor,
            "user_name": user.name,
            "user_avatar": user.avatar
        }
