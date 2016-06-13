# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0018_list_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, default=''),
        ),
    ]
