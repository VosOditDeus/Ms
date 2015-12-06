# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('photo', '0007_auto_20151205_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumbnail2',
            field=models.ImageField(null=True, upload_to=b'media/', blank=True),
        ),
    ]
