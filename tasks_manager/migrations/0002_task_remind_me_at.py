# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 15:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='remind_me_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 23, 15, 29, 44, 841454, tzinfo=utc)),
            preserve_default=False,
        ),
    ]