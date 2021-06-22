# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 23 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""

from apscheduler.schedulers.background import BackgroundScheduler

from app.tasks.video_tasks import current_video_count_task

def start_scheduler():
    notification_scheduler = BackgroundScheduler()
    notification_scheduler.add_job(current_video_count_task, "interval", minutes=1,
                                   id='video_count_task', replace_existing=True)
    notification_scheduler.start()
    #self.scheduler = APScheduler()
    # scheduler.api_enabled = True
    # scheduler.init_app(self.app)
    # scheduler.start()
    # scheduler.add_job(func=ping_server_auto, id=self.service_name, trigger='interval', seconds=3)