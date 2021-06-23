# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 23 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from datetime import datetime
from flask_admin.contrib.peewee import ModelView
from flask_admin.model import typefmt

from app import app, Video


def date_format(view, value):
    return value.strftime('%d.%m.%Y')


def format_datetime(view, value):
    return value.strftime('%a %I:%M %p, %b %d, %Y')


MY_DEFAULT_FORMATTERS = dict(typefmt.BASE_FORMATTERS)
MY_DEFAULT_FORMATTERS.update({
    type(None): typefmt.null_formatter,
    # datetime.date: date_format
    datetime.date: format_datetime
})


class VideoAdmin(ModelView):
    page_size = 20
    can_set_page_size = True
    column_formatters = MY_DEFAULT_FORMATTERS
    can_create = False
    can_view_details = True
    column_default_sort = ('last_edited', 'id')
    column_exclude_list = [
        'tags,'
        'view_count',
        'like_count',
        'dislike_count',
        'comment_count',
        'duration',
        'created',
        'last_edited',
        'fetch_count'
    ]

    column_filters = [
        'channel_id',
        'video_id',
        'title',
        'tags',
        'view_count',
        'like_count',
        'dislike_count',
        'comment_count',
        'duration',
        'created',
        'last_edited',
        'fetch_count',
    ]
    column_search = [
        'channel_id',
        'video_id',
        'title',
        'tags'
    ]


import flask_admin as admin

admin = admin.Admin(app,
                    name='Sixads Video Fetcher 1.0.0',
                    template_mode='bootstrap4'
                    )
admin.add_view(VideoAdmin(Video))
