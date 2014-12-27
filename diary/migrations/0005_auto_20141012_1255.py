# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_auto_20141012_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventlocation',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventlocation',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
