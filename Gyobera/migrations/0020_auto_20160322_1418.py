# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0019_booking_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Gender',
            field=models.CharField(default='--', choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
