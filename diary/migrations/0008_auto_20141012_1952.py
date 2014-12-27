# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0007_auto_20141012_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageitem',
            name='data',
            field=models.ImageField(upload_to=b'images'),
        ),
    ]
