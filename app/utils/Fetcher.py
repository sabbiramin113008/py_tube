# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 20 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from app import db
from app.models import RelativeQuotaCount
from app_config import API_KEY
import pyyoutube as ptube

'''
A read operation that retrieves a list of resources -- channels, videos, playlists -- usually costs 1 unit.
A write operation that creates, updates, or deletes a resource usually has costs 50 units.
A search request costs 100 units.
'''


class Fetcher:
    def __init__(self):
        self.api_key = API_KEY
        self.api = ptube.Api(api_key=self.api_key)


    def get_all_videos(self, channel_id, limit=50, count=50):
        db.connect()
        videos = list()
        try:
            print('Starting Fetching the Data for Channel:', channel_id)
            response = self.api.search(channel_id=channel_id, limit=limit, count=count)
            try:
                rqc = RelativeQuotaCount(op_name='search', unit_spent=50).save()
            except:
                pass
            next_page_token = response.nextPageToken
            while next_page_token:
                for res in response.items:
                    if res.id.videoId:
                        videos.append(res.id.videoId)
                next_page_token = response.nextPageToken
                response = self.api.search(
                    channel_id=channel_id,
                    limit=limit,
                    count=count,
                    page_token=next_page_token
                )
                try:
                    rqc = RelativeQuotaCount(op_name='search', unit_spent=50).save()
                except:
                    pass
        except Exception as e:
            print('Error Getting Data:', e)
        db.close()
        return videos
