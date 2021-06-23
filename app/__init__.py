# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 20 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""

import logging
from flask import Flask
from flask_cors import CORS
from peewee import MySQLDatabase

from app_config import *

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
cors = CORS(app)
if APP_ENV == 'DEV':
    app.config.from_object('app_config.DevConfig')
else:
    app.config.from_object('app_config.TestConfig')

db = MySQLDatabase(
    app.config.get('DATABASE_NAME'),
    user=app.config.get('DATABASE_USER'),
    password=app.config.get('DATABASE_PASSWORD'),
    host=app.config.get('DATABASE_HOST'),
    port=app.config.get('DATABASE_PORT')
)


@app.before_request
def _db_connect():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()


from .api.video import *
from .dashboard import *
