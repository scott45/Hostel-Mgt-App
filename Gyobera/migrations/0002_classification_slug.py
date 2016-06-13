# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classification',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
