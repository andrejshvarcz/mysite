# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 13:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 13, 16, 37, 20965, tzinfo=utc)),
        ),
    ]