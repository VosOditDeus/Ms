# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('photo', '0005_auto_20151203_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='album',
        ),
        migrations.AddField(
            model_name='image',
            name='album',
            field=models.ManyToManyField(to='photo.Album', blank=True),
        ),
    ]
