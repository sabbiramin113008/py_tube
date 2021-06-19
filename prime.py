# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 19 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
import pyyoutube
import pyyoutube as ptube

from app_config import API_KEY

api = ptube.Api(api_key=API_KEY)

# channel_name = 'googledevelopers'
channel_name = 'RnaRTuminoL'


def get_videos(channel_name):
    api = pyyoutube.Api(api_key=API_KEY)
    channel_res = api.get_channel_info(channel_name=channel_name)


    playlist_id = channel_res.items[0].contentDetails.relatedPlaylists.uploads

    playlist_item_res = api.get_playlist_items(
        playlist_id=playlist_id, count=10, limit=6
    )

    videos = []
    for item in playlist_item_res.items:
        video_id = item.contentDetails.videoId
        video_res = api.get_video_by_id(video_id=video_id)
        videos.extend(video_res.items)
    return videos


channel_response = api.get_channel_info(channel_name=channel_name)
channel_response = api.get_channel_info(channel_id='UC1ZRNf5khuJFrtacQsFqV6w')

contentDetails = channel_response.items[0].contentDetails
playlist_id = contentDetails.relatedPlaylists.uploads
playlist_items_response = api.get_playlist_items(playlist_id=playlist_id, count=10, limit=6)
videos = list()
for item in playlist_items_response.items:
    video_id = item.contentDetails.videoId
    video_response = api.get_video_by_id(video_id=video_id)
    videos.append(video_response.items[0].contentDetails.duration)

print (videos)
