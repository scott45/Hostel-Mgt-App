# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0004_booking_hostel'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Room_capacity',
            field=models.CharField(max_length=1, default='', choices=[('M', 'Single'), ('F', 'Double')]),
        ),
    ]
