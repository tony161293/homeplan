# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.TextField()),
                ('product_price', models.IntegerField(default=0)),
                ('product_image', models.ImageField(upload_to=b'product')),
                ('product_brand', models.ForeignKey(blank=True, to='backend.Brand', null=True)),
                ('product_category', models.ForeignKey(blank=True, to='backend.Category', null=True)),
                ('product_feature', models.ForeignKey(blank=True, to='backend.Group', null=True)),
            ],
        ),
    ]
