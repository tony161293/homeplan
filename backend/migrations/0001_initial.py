# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand_name', models.CharField(max_length=100)),
                ('brand_code', models.CharField(max_length=100)),
                ('brand_image', models.ImageField(upload_to=b'brand')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=300)),
                ('category_code', models.CharField(max_length=100)),
                ('category_image', models.ImageField(upload_to=b'category')),
                ('category_parent', models.ForeignKey(blank=True, to='backend.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=100)),
                ('group_priority', models.IntegerField(default=0)),
            ],
        ),
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
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supplier_name', models.CharField(max_length=100)),
                ('supplier_person', models.CharField(max_length=100)),
                ('supplier_title', models.CharField(max_length=100)),
                ('supplier_paddress', models.TextField()),
                ('supplier_saddress', models.TextField()),
                ('supplier_city', models.CharField(max_length=100)),
                ('supplier_state', models.CharField(max_length=100)),
                ('supplier_pin', models.IntegerField(default=0)),
                ('supplier_country', models.CharField(max_length=100)),
                ('supplier_phone', models.IntegerField(default=0)),
                ('supplier_fax', models.IntegerField(default=0)),
                ('supplier_email', models.EmailField(max_length=254)),
                ('supplier_url', models.URLField()),
                ('supplier_notes', models.TextField()),
                ('supplier_image', models.ImageField(upload_to=b'supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sales_order_id', models.IntegerField(default=0)),
                ('order_date', models.DateTimeField()),
                ('project_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('product_quality', models.CharField(max_length=400)),
                ('remarks', models.TextField()),
            ],
        ),
    ]
