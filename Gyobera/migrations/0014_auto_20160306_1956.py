# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0013_auto_20160306_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='Book_id',
        ),
        migrations.AddField(
            model_name='booking',
            name='Book_No',
            field=models.IntegerField(default=1),
        ),
    ]
