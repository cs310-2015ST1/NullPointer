# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('date_id', models.DateField(serialize=False, primary_key=True)),
                ('weather_string', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
