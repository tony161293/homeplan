# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_auto_20151225_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='supplier_image',
            field=models.ImageField(default=datetime.datetime(2015, 12, 25, 18, 38, 2, 604442, tzinfo=utc), upload_to=b'supplier'),
            preserve_default=False,
        ),
    ]
