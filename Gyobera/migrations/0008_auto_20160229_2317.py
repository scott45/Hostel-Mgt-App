# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0007_auto_20160229_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Book_id',
            field=models.CharField(max_length=5, default=''),
        ),
        migrations.AddField(
            model_name='room',
            name='Room_Number',
            field=models.CharField(max_length=50, default=''),
        ),
    ]
