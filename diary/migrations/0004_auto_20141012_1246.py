# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_auto_20141012_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlocation',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
