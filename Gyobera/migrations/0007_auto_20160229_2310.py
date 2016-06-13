# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0006_auto_20160227_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='Book_id',
        ),
        migrations.RemoveField(
            model_name='room',
            name='Room_Number',
        ),
    ]
