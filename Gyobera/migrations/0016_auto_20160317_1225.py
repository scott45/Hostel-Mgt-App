# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0015_mobilepayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobilepayment',
            name='Amount_deposited',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mobilepayment',
            name='Mobile_No',
            field=models.IntegerField(default='07'),
        ),
    ]
