# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonApp', '0020_auto_20180306_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admin_role',
            field=models.IntegerField(default=0),
        ),
    ]