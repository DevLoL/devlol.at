# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0009_diaryitem_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaryitem',
            name='link',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
