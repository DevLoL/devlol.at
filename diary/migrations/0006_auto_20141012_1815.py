# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diary', '0005_auto_20141012_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaryitem',
            name='author',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imageitem',
            name='diary_item',
            field=models.ForeignKey(default=None, to='diary.DiaryItem'),
            preserve_default=False,
        ),
    ]
