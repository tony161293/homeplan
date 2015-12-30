# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_supplier_supplier_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_parent',
            field=models.IntegerField(default=0),
        ),
    ]
