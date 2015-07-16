# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0002_userprofile_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place_name', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=30)),
                ('lng', models.CharField(max_length=30)),
                ('content_string', models.CharField(max_length=200)),
                ('user_profile', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='favorites',
            field=models.ManyToManyField(related_name='favorited_by', to='login.Favorite'),
            preserve_default=True,
        ),
    ]
