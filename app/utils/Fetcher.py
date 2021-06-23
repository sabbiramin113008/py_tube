# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 20 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from app import db
from app.models import RelativeQuotaCount, Video, utcnow_aware
from app.utils.DbContextManager import db_handler
from app_config import Config
import pyyoutube as ptube

'''
A read operation that retrieves a list of resources -- channels, videos, playlists -- usually costs 1 unit.
A write operation that creates, updates, or deletes a resource usually has costs 50 units.
A search request costs 100 units.
'''


class Fetcher:
    def __init__(self):
        self.api_key = Config.API_KEY
        self.api = ptube.Api(api_key=self.api_key)


    def get_all_videos(self, channel_id, limit=50, count=50):
        videos = list()
        with db_handler():

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
        return videos

    def get_video_by_id(self, video_id):

       try:
           res = self.api.get_video_by_id(video_id=video_id)
           snip = res.items[0].snippet
           stts = res.items[0].statistics
           content = res.items[0].contentDetails
           tags = snip.tags
           title = snip.title
           view_count = stts.viewCount
           like_count = stts.likeCount
           dislike_count = stts.dislikeCount
           comment_count = stts.commentCount
           m = int(content.duration.split('M')[0].replace('PT', '')) * 60
           sec = int(content.duration.split('M')[1].replace('S', ''))
           duration = m + sec

           try:
               v, isCreated = Video.get_or_create(video_id=video_id)
               pre_fetch_count = v.fetch_count
               v.title = title
               v.tags = tags
               v.view_count = view_count
               v.like_count = like_count
               v.dislike_count = dislike_count
               v.comment_count = comment_count
               v.duration = duration
               v.fetch_count = pre_fetch_count + 1
               v.last_edited = utcnow_aware
               v.save()
               print('Successfully Updated video Id:', video_id)
               try:
                   rqc = RelativeQuotaCount(op_name='get_list', unit_spent=1).save()
               except:
                   pass

           except Exception as e:
               print('Error Saving Video Data:', e)
       except:
           pass

if __name__=='__main__':
    video_id = 'E1aybmBrT_M'
    video_id = 'UDtmAKq_PZg'
    f = Fetcher()
    f.get_video_by_id(video_id)