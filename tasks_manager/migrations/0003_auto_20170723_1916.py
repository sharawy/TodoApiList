# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 17:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_manager', '0002_task_remind_me_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='TodoTask',
        ),
    ]
