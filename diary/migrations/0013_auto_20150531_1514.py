# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0012_auto_20150525_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageitem',
            name='data',
        ),
        migrations.AddField(
            model_name='imageitem',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
