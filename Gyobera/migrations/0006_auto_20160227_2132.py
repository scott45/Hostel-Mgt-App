# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0005_booking_room_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Hostel',
            field=models.ForeignKey(default='--', to='Gyobera.List'),
        ),
    ]
