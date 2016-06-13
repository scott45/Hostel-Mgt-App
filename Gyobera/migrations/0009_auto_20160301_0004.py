# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0008_auto_20160229_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Book_id',
            field=models.IntegerField(default='001'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='Room_capacity',
            field=models.CharField(choices=[('S', 'Single'), ('D', 'Double')], max_length=1, default=''),
        ),
        migrations.AlterField(
            model_name='room',
            name='Room_Number',
            field=models.IntegerField(default='001'),
        ),
    ]
