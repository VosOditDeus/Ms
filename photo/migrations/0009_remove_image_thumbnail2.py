# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('photo', '0008_image_thumbnail2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='thumbnail2',
        ),
    ]
