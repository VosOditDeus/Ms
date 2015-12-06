# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('photo', '0006_auto_20151203_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='album',
            new_name='albums',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='likes',
            new_name='rating',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=b'media/'),
        ),
    ]
