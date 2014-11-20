__author__ = 'badpoet'

class Barrage(object):

    def __init__(self, video_id, user_id, content, position, mode, size, color, pool, stamp):
        self.video_id = video_id
        self.user_id = user_id
        self.content = content
        self.position = position
        self.mode = mode
        self.size = size
        self.color = color
        self.pool = pool
        self.stamp = stamp

    def to_dict(self):
        return {
            "video_id": self.video_id,
            "user_id": self.user_id,
            "content": self.content,
            "position": self.position,
            "mode": self.mode,
            "size": self.size,
            "color": self.color,
            "pool": self.pool,
            "stamp": self.stamp
        }