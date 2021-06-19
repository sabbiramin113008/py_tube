# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 19 Jun 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""


import os

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
API_KEY = os.getenv('API_KEY')

print (API_KEY
       )