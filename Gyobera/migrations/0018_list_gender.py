# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0017_mobilepayment_pin_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='', max_length=1),
        ),
    ]
