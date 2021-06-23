# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 23 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
import datetime
from playhouse.shortcuts import model_to_dict

from app import db
from app.models import Video, RelativeQuotaCount, utcnow_aware
from app.utils.DbContextManager import db_handler
from app.utils.Fetcher import Fetcher
from app_config import API_CALL_MAX_LIMIT


def current_video_count_task():
    with db_handler():
        try:
            count = Video.select().count()
        except:
            count = 0
        print('Total Videos:', count)


def update_videos():
    f = Fetcher()
    with db_handler():
        # Todo:// Improve fetching logic, consider api quota limit, relativeQuotaCount and optimal selecting
        today = utcnow_aware.today()
        yesterday = today - datetime.timedelta(days=1)
        tomorrow = today + datetime.timedelta(days=1)

        possible_call_count = 0
        try:
            total_quota_spent = RelativeQuotaCount.select().where(RelativeQuotaCount.created > yesterday,
                                                                  RelativeQuotaCount.created < tomorrow).count()
        except Exception as e:
            print('Error in RelativeQuotaCount:', e)
            total_quota_spent = 0

        remaining_call_count = API_CALL_MAX_LIMIT - total_quota_spent
        try:
            total_video_count = Video.select().count()
        except:
            total_video_count = 0
        if total_video_count > remaining_call_count:
            possible_call_count = total_video_count - remaining_call_count
            videos = Video.select().paginate(1, possible_call_count).order_by('-last_edited','view_count')
        else:
            videos = Video.select()
        print(total_quota_spent, total_video_count, possible_call_count)
        for v in videos:
            video_id = v.video_id
            print(model_to_dict(v))
            f.get_video_by_id(video_id=video_id)

