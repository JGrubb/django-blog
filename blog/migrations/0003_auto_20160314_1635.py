# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Published at'),
        ),
    ]
