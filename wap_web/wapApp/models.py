# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import ordering as ordering
from django.contrib import admin
import django.utils.timezone as timezone
from django.db import models
# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=55)
    password = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    is_active = models.IntegerField(default=0)
    add_date = models.IntegerField('注册日期',default=0)
    active_date = models.IntegerField('激活', default=0)
    class meta:
        ordering=['-add_date']





