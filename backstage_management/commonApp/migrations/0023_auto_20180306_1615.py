# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonApp', '0022_auto_20180306_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='admin_role',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
