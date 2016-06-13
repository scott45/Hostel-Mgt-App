# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0011_auto_20160306_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='Price_double',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='room',
            name='Price_single',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='room',
            name='Total_rooms',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='Book_id',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='booking',
            name='Booked_by',
            field=models.ForeignKey(to='Gyobera.Student', default=''),
        ),
        migrations.AlterField(
            model_name='room',
            name='Room_Number',
            field=models.CharField(max_length=50),
        ),
    ]
