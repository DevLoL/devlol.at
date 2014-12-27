# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20141012_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaryitem',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]
