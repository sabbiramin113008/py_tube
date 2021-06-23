# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 23 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
import operator
from flask import request, jsonify
from playhouse.shortcuts import model_to_dict
from webargs import fields
from webargs.flaskparser import use_args
from wtfpeewee._compat import reduce

from app import app
from app.models import Video

user_args = {
    'page': fields.Int(missing=1),
    'size': fields.Int(missing=30),
    'tags': fields.DelimitedList(fields.Str()),
    'view_count_lt': fields.Int(required=False),
    'view_count_gt': fields.Int(required=False),
    'view_count_eq': fields.Int(required=False),
    'like_count_lt': fields.Int(required=False),
    'like_count_gt': fields.Int(required=False),
    'like_count_eq': fields.Int(required=False),
    'comment_count_lt': fields.Int(required=False),
    'comment_count_gt': fields.Int(required=False),
    'comment_count_eq': fields.Int(required=False),

}


@app.route('/api/v1/videos', methods=['GET'])
@use_args(user_args, location='query')
def get_videos(args):
    page = args.get('page')
    size = args.get('size')
    tags = args.get('tags')
    view_count_lt = args.get('view_count_lt')
    view_count_gt = args.get('view_count_gt')
    view_count_eq = args.get('view_count_eq')
    like_count_lt = args.get('like_count_lt')
    like_count_gt = args.get('like_count_gt')
    like_count_eq = args.get('like_count_eq')
    comment_count_lt = args.get('comment_count_lt')
    comment_count_gt = args.get('comment_count_gt')
    comment_count_eq = args.get('comment_count_eq')
    dislike_count_lt = args.get('dislike_count_lt')
    dislike_count_gt = args.get('dislike_count_gt')
    dislike_count_eq = args.get('dislike_count_eq')

    sql_clause = list()
    for k, v in args.items():
        if view_count_eq:
            sql_clause.append(Video.view_count == view_count_eq)
        if view_count_lt:
            sql_clause.append(Video.view_count > view_count_lt)
        if view_count_gt:
            sql_clause.append(Video.view_count > view_count_gt)
        if tags:
            for tag in tags:
                sql_clause.append(Video.tags.contains(tag))
        if like_count_lt:
            sql_clause.append(Video.like_count < like_count_lt)
        if like_count_gt:
            sql_clause.append(Video.like_count > like_count_gt)
        if like_count_eq:
            sql_clause.append(Video.like_count == like_count_eq)
        if comment_count_lt:
            sql_clause.append(Video.comment_count < comment_count_lt)
        if comment_count_gt:
            sql_clause.append(Video.comment_count > comment_count_gt)
        if comment_count_eq:
            sql_clause.append(Video.comment_count == comment_count_eq)
        if dislike_count_lt:
            sql_clause.append(Video.dislike_count < dislike_count_lt)
        if dislike_count_gt:
            sql_clause.append(Video.dislike_count > dislike_count_gt)
        if dislike_count_eq:
            sql_clause.append(Video.dislike_count == dislike_count_eq)

    try:
        exp = reduce(operator.and_, sql_clause)
    except Exception as e:
        print('Error Compressing SQL:', e)
        exp = None

    if exp:
        queryset = Video.select().where(exp).paginate(page, size)
    else:
        queryset = Video.select().paginate(page, size)
    models = [model_to_dict(r) for r in queryset]
    response = dict()
    response['count'] = len(models)
    response['models'] = models
    return jsonify(response)
