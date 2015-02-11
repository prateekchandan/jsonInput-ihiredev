# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonInput.models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonInput', '0002_auto_20150207_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessKeys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userId', models.CharField(max_length=500)),
                ('AccessToken', models.CharField(default=jsonInput.models.AccessTokenGenerate, max_length=1000)),
                ('SecretKey', models.CharField(default=jsonInput.models.SecretKeyGenerate, max_length=50)),
            ],
            options={
                'verbose_name_plural': 'AccessKeys',
            },
            bases=(models.Model,),
        ),
    ]
