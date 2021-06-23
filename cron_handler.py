# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 23 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""

from apscheduler.schedulers.background import BackgroundScheduler
from app_config import CRON_INTERVAL_MINUTES
from app.tasks.video_tasks import current_video_count_task, update_videos

def start_scheduler():
    notification_scheduler = BackgroundScheduler()
    notification_scheduler.add_job(current_video_count_task, "interval", minutes=10,
                                   id='video_count_task', replace_existing=True)
    notification_scheduler.add_job(update_videos, "interval", minutes=CRON_INTERVAL_MINUTES,
                                   id='video_update_task', replace_existing=True)
    notification_scheduler.start()
