# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonApp', '0011_auto_20180306_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.IntegerField(choices=[(0, '保密'), (1, '男'), (2, '女')], max_length=2),
        ),
    ]
