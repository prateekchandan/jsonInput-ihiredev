# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonInput.models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonInput', '0003_accesskeys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesskeys',
            name='SecretKey',
            field=models.CharField(default=jsonInput.models.SecretKeyGenerate, max_length=1000),
            preserve_default=True,
        ),
    ]
