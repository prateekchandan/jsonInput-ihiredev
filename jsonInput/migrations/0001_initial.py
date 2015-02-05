# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='payments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blockId', models.IntegerField()),
                ('sourceTxid', models.CharField(max_length=500)),
                ('sourceAddress', models.TextField()),
                ('destinationAddress', models.CharField(max_length=1000)),
                ('outAsset', models.TextField(max_length=500)),
                ('outAmount', models.BigIntegerField()),
                ('status', models.CharField(max_length=200)),
                ('lastUpdatedBlockId', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
