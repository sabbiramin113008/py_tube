# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 20 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
import datetime
from peewee import *
import pytz

from app import db

class BaseModel(Model):
    class Meta:
        database = db

utcnow = datetime.datetime.utcnow()
utcnow_aware = utcnow.replace(tzinfo=pytz.utc)

class Video(BaseModel):
    channel_id = CharField(null=False)
    video_id = CharField(null=False, unique=True)
    title = CharField(null=True)
    tags = TextField(null=True)
    view_count = IntegerField(default=0)
    like_count = IntegerField(default=0)
    dislike_count = IntegerField(default=0)
    comment_count = IntegerField(default=0)
    duration = IntegerField(default=0) # PT1M33S -> in-seconds
    created = DateTimeField(default=utcnow_aware)
    last_edited = DateTimeField(null=True)
    fetch_count = IntegerField(default=0)

    class Meta:
        table_name = 'tbl_video'

class RelativeQuotaCount(BaseModel):
    created = DateTimeField(default=utcnow_aware)
    op_name = CharField(null=False) # op_name: Operation name : [enlist of resources like channel, videos, playlists
    unit_spent = IntegerField(null=False)

    class Meta:
        table_name = 'tbl_relativequotacount'





