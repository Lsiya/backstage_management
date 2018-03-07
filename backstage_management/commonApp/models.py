# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    sex = models.IntegerField(default=0)
    phone = models.CharField(max_length=30,unique=True)
    email = models.EmailField(max_length=30)
    note = models.CharField(max_length=100)
    admin_role = models.CharField(max_length=50, default='保密')
    add_date = models.DateTimeField('保存日期', default=timezone.now)
    mod_date = models.DateTimeField('最后修改日期',null=True)