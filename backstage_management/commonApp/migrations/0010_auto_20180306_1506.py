# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonApp', '0009_auto_20180306_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
