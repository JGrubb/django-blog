# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-04 14:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160315_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 5, 4, 14, 49, 58, 607842, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 4, 14, 50, 6, 815663, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
