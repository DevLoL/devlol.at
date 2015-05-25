# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0011_auto_20150512_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diaryitem',
            old_name='date',
            new_name='start_date',
        ),
        migrations.RenameField(
            model_name='diaryitem',
            old_name='time',
            new_name='start_time',
        ),
        migrations.AddField(
            model_name='diaryitem',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 25, 1, 51, 29, 554374)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diaryitem',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2015, 5, 25, 1, 51, 42, 109918)),
            preserve_default=False,
        ),
    ]
