# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonApp', '0012_auto_20180306_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('s', '保密'), ('m', '男'), ('f', '女')], max_length=2),
        ),
    ]
