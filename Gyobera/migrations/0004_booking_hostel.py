# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0003_auto_20160210_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Hostel',
            field=models.ForeignKey(default='', to='Gyobera.List'),
        ),
    ]
