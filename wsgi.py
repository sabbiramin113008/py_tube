# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 19 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from app import app
from cron_handler import start_scheduler

if __name__=='__main__':
    start_scheduler()
    app.run(
        host='localhost',
        port=5003,
        debug=True
    )