#!/usr/bin/python3

# must setup django env from standalone script.
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()

from decimal import Decimal
import logging
import datetime as dt
import json

from myapp.models import *

# -----------------------------------------------------------------------
# 使用uwsgi启动一个定时任务,每天定时执行
def cronjob():
    logging.info("start cronjob.")    
    logging.info("end cronjob.")

try:
    cronjob()
except Exception as e:
    logging.error("start cronjob error: %s" % str(e))



