# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default=datetime.datetime(2015, 12, 24, 20, 58, 3, 93291, tzinfo=utc), upload_to=b'category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='category_parent',
            field=models.CharField(max_length=100),
        ),
    ]
