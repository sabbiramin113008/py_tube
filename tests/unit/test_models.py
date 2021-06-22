# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 23 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
import unittest
from app.models import Video

class VideoModelInsertionTest(unittest.TestCase):
    def test_adding_new_video(self):
        """
           GIVEN a Video model
           WHEN a new Video is created
           THEN check the channel_id, video_id fields are defined correctly
        """
        channel_id = 'UC1ZRNf5khuJFrtacQsFqV6w'
        video_id = 'YrKIgalEgdo'

        video = Video(channel_id=channel_id,video_id=video_id)
        self.assertEqual(video.channel_id,channel_id)
        self.assertEqual(video.video_id,video_id)


if __name__=='__main__':
    unittest.main()