__author__ = 'badpoet'

import pymongo
from bson.objectid import ObjectId

from youmu.config import DefaultConfig

class MongoClient(object):

    def __init__(self, host = DefaultConfig.MONGO_HOST, port = DefaultConfig.MONGO_PORT):
        self.db = pymongo.Connection(host, port)["youmu"]
        # self.db.authenticate(username, password)
        self.user_col = self.db["user"]
        self.video_col = self.db["video"]
        self.video_like_col = self.db["video_like"]
        self.comment_col = self.db["comment"]
        self.comment_floor_ctrl_col = self.db["floor_ctrl"]

    # ABOUT USER

    def has_user_id(self, user_id):
        return self.user_col.find_one({"id": user_id}) is not None

    def get_user_by_id(self, user_id):
        return self.user_col.find_one({"id": user_id})

    def get_user_by_mid(self, user_mongo_id):
        return self.user_col.find_one({"_id": ObjectId(user_mongo_id)})

    def insert_user(self, user_dict):
        self.user_col.insert(user_dict)

    def update_user(self, user_dict):
        self.user_col.update(
            { "_id": user_dict["_id"] },
            user_dict
        )

    # ABOUT VIDEO

    def get_video_by_id(self, video_id):
        return self.video_col.find_one({"video_id": video_id})

    def get_video_list(self, offset = 0, size = 10):
        return self.video_col.find()[offset : size]

    def get_ordered_video_list(self, query, offset = 0, size = 10, order_by = "upload_time", reverse = False):
        query = {
            "$query": query,
            "$orderby": { order_by: -1 if reverse else 1 }
        }
        return self.video_col.find(query)[offset : size]

    def add_video_play_count(self, id):
        self.video_col.update(
            { "video_id": id },
            { "$inc": { "play_count": 1 } }
        )

    def create_like_info(self, user_id, video_id):
        self.video_like_col.insert(
            { "user_id": user_id, "video_id": video_id }
        )
        self.video_col.update(
            { "video_id": video_id },
            { "$inc": { "like": 1 } }
        )

    def delete_like_info(self, user_id, video_id):
        self.video_like_col.remove(
            { "user_id": user_id, "video_id": video_id }
        )
        self.video_col.update(
            { "video_id": video_id },
            { "$inc": { "like": -1} }
        )

    def query_like_info(self, user_id, video_id):
        return (self.video_like_col.find_one(
            { "user_id": user_id, "video_id": video_id }
        ) is not None)

    def query_like_info_by_user(self, user_id):
        return self.video_like_col.find(
            { "user_id": user_id }
        )

    def query_like_info_by_video(self, video_id):
        return self.video_like_col.find(
            { "video_id": video_id }
        )

    def count_like_info_by_user(self, user_id):
        return self.video_like_col.find(
            { "user_id": user_id }
        ).count()

    def count_like_info_by_video(self, video_id):
        return self.video_like_col.find(
            { "video_id": video_id }
        ).count()

    # ABOUT COMMENT

    def assign_comment_floor(self, video_id):
        tmp = self.comment_floor_ctrl_col.find_and_modify(
            query = { "video_id": video_id },
            update = { "$inc": { "floor_cnt": 1 } },
            new = True,
            upsert = True
        )
        return int(tmp["floor_cnt"])

    def insert_comment(self, comment):
        self.comment_col.insert(comment)

    def get_comment_by_video_id(self, video_id, offset, size):
        return self.comment_col.find({
            "$query": { "video_id": video_id },
            "$orderby": { "floor": 1 }
        })[offset : size]

    def get_comment_by_user_id(self, user_id, offset, size, reverse):
        return self.comment_col.find({
            "$query": { "user_id": user_id },
            "$orderby": { "reply_time": -1 if reverse else 1 }
        })[offset : size]