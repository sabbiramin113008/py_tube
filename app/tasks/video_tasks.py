# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 23 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from app import db
from app.models import Video
from app.utils.DbContextManager import db_handler


def current_video_count_task():
    with db_handler():
        try:
            count = Video.select().count()
        except:
            count = 0
        print ('Total Videos:', count)


