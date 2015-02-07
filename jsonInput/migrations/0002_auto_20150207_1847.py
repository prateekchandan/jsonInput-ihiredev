# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jsonInput', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payments',
            options={'verbose_name_plural': 'payments'},
        ),
    ]
