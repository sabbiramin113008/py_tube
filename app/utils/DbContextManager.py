# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 23 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
import contextlib
from playhouse.shortcuts import model_to_dict

from app import db
from app.models import Video


@contextlib.contextmanager
def db_handler():
    try:
        db.connect()
        yield
    except Exception as e:
        print ('Error Connecting Db:', e)
    finally:
        db.close()
