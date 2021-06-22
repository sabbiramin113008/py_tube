# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 20 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from app import db
from app.models import Video
from app.utils.Fetcher import Fetcher
from app_config import Config

if __name__ == '__main__':
    channel_id = Config.DEFAULT_CHANNEL_ID
    fetcher = Fetcher()
    videos = fetcher.get_all_videos(channel_id=channel_id)
    db.connect()
    for v in videos:
        try:
            v = Video(
                channel_id=channel_id,
                video_id=v
            )
            v.save()
        except Exception as e:
            print('Error Saving Data for video Id: ', v, ' Error:', str(e))

    db.close()
