# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-17 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wapApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=55)),
                ('password', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=30)),
                ('is_active', models.IntegerField(default=0)),
                ('add_date', models.IntegerField(default=0, verbose_name='注册日期')),
                ('active_date', models.IntegerField(default=0, verbose_name='激活')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
