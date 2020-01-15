from django.db import models
from django.db.models import Sum
import datetime as dt
from datetime import datetime
from django.utils import timezone
import logging
from decimal import Decimal
import traceback

from myproject.settings import BASE_ADDRESS


class Sale(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

class Client(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    identity = models.CharField(max_length=255)
    card = models.CharField(max_length=255)
    up = models.ForeignKey('self', related_name='down', null=True, on_delete=models.DO_NOTHING)
    up_redpacket = models.BooleanField(default=False)
    sale = models.ForeignKey(Sale, related_name='client', null=True, on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def json(self):        
        self.__dict__.pop("_state")
        return self.__dict__

