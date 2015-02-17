# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20150217_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(max_length=5500),
            preserve_default=True,
        ),
    ]
