# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jsonInput', '0004_auto_20150211_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='outAmount',
            field=models.DecimalField(max_digits=16, decimal_places=8),
            preserve_default=True,
        ),
    ]
