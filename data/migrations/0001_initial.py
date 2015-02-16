# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=150)),
                ('url', models.CharField(max_length=150, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('url', models.CharField(max_length=150, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to=b'prodimages')),
                ('desc', models.TextField(max_length=2000)),
                ('cat', models.ForeignKey(to='data.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
