# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0008_auto_20141012_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaryitem',
            name='subtitle',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
