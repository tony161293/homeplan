# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20151224_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(upload_to=b'category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_parent',
            field=models.IntegerField(max_length=100),
        ),
    ]
