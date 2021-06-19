# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 19 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""

import os

from dotenv import load_dotenv

load_dotenv()

# Youtube API V3 API-KEY
API_KEY = os.getenv('API_KEY')


# App Config
APP_SECRET = os.getenv('APP_SECRET')

# Database
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = int(os.getenv('DATABASE_PORT'))

#Default Timezone
DEFAULT_TIMEZONE = 'America/Montreal'
DEFAULT_DATETIME_FORMAT = '%Y:%m:%d %H:%M:%S %Z %z'

# channel Id
DEFAULT_CHANNEL_ID = os.getenv('DEFAULT_CHANNEL_ID')