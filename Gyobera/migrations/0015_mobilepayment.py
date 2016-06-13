# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0014_auto_20160306_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobilePayment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('Booked_by', models.ForeignKey(default='--', to='Gyobera.Student')),
                ('Hostel', models.ForeignKey(to='Gyobera.List', blank=True, null=True)),
            ],
        ),
    ]
