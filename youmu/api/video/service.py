#!/usr/bin/env python

"""Backend video management module.
"""

from youmu.clients.mongoclient import MongoClient

__author__ = 'badpoet, ampersand'

mongo = MongoClient()


class VideoService(object):

    @staticmethod
    def get_video_by_id(vid):
        return mongo.get_video_by_id(vid)

    @staticmethod
    def delete_video_by_id(vid):
        return mongo.delete_video_by_id(vid)

