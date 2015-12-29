# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supplier_name', models.CharField(max_length=100)),
                ('supplier_person', models.CharField(max_length=100)),
                ('supplier_title', models.CharField(max_length=100)),
                ('supplier_paddress', models.TextField()),
                ('supplier_sadress', models.TextField()),
                ('supplier_city', models.CharField(max_length=100)),
                ('supplier_state', models.CharField(max_length=100)),
                ('supplier_pin', models.IntegerField(default=0)),
                ('supplier_country', models.CharField(max_length=100)),
                ('supplier_phone', models.IntegerField(default=0)),
                ('supplier_fax', models.IntegerField(default=0)),
                ('supplier_email', models.EmailField(max_length=254)),
                ('supplier_url', models.URLField()),
                ('supplier_notes', models.TextField()),
            ],
        ),
    ]
