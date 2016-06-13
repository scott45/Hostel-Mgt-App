# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0010_auto_20160301_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='Price_double',
        ),
        migrations.RemoveField(
            model_name='room',
            name='Price_single',
        ),
        migrations.RemoveField(
            model_name='room',
            name='Total_rooms',
        ),
        migrations.AddField(
            model_name='booking',
            name='Book_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='booking',
            name='Booked_by',
            field=models.ForeignKey(null=True, blank=True, to='Gyobera.Student'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='Hostel',
            field=models.ForeignKey(null=True, blank=True, to='Gyobera.List'),
        ),
        migrations.AlterField(
            model_name='room',
            name='Room_Number',
            field=models.IntegerField(default=1),
        ),
    ]
