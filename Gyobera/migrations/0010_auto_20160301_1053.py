# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0009_auto_20160301_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='Book_id',
        ),
        migrations.AlterField(
            model_name='room',
            name='Room_Number',
            field=models.IntegerField(default='1'),
        ),
    ]
