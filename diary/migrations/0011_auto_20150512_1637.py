# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0010_diaryitem_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaryitem',
            name='link',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='diaryitem',
            name='subtitle',
            field=models.CharField(max_length=64, blank=True),
            preserve_default=True,
        ),
    ]
