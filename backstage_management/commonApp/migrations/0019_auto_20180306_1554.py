# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonApp', '0018_auto_20180306_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.IntegerField(default=0, max_length=5),
        ),
    ]
