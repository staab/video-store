# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='title',
            field=models.CharField(default='x', max_length=255),
            preserve_default=False,
        ),
    ]
