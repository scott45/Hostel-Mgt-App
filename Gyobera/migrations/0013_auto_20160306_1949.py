# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0012_auto_20160306_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Booked_by',
            field=models.ForeignKey(to='Gyobera.Student', default='--'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='Room_capacity',
            field=models.CharField(max_length=1, default='--', choices=[('S', 'Single'), ('D', 'Double')]),
        ),
    ]
