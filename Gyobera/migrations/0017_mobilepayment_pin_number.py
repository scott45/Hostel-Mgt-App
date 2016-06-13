# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyobera', '0016_auto_20160317_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobilepayment',
            name='Pin_Number',
            field=models.IntegerField(default=0),
        ),
    ]
