# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popularity',
            name='lat',
            field=models.DecimalField(max_digits=12, decimal_places=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='popularity',
            name='lng',
            field=models.DecimalField(max_digits=12, decimal_places=8),
            preserve_default=True,
        ),
    ]
