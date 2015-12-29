# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_supplier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='supplier_sadress',
            new_name='supplier_saddress',
        ),
    ]
