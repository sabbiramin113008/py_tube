# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 20 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from app import db
from app.models import Video, RelativeQuotaCount


def init_db():
    tables = [
     Video, RelativeQuotaCount
    ]
    try:
        db.drop_tables(models=tables)
        db.create_tables(models=tables)
        print ('Database Created Successfully')
    except Exception as e:
        raise e


if __name__ == '__main__':
    init_db()