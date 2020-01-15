from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, StreamingHttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import logging
import json
import traceback
import hashlib
import requests
from datetime import datetime
from decimal import Decimal

from .models import *
from myproject.settings import BASE_ADDRESS, BASE_DIR


# return json resp util func
# 0: success, 1: error
def jsonResp(code=0, errmsg='', result=None):
    resp = HttpResponse(content=json.dumps(
        obj={"code": code, "errmsg": errmsg, "result": result},
        cls=DjangoJSONEncoder)
    )
    resp['Cache-Control'] = 'no-cache'
    resp['mimetype'] = 'application/json'
    resp["Content-Type"] = "application/json;charset=utf-8"
    return resp


# exceptin decorator func    
def catch_exception(func):
    def new_func(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            result = jsonResp(code=1, errmsg=str(e))
            logging.error('\033[35m %s \033[0m', traceback.format_exc())
        return result
    return new_func


@catch_exception
def index(request):
    return HttpResponse("Hello, world.")



