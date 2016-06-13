# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Gyobera', '0002_classification_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('About_me', models.CharField(max_length=200)),
                ('picture', models.ImageField(upload_to='profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='classification',
            name='likes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='classification',
            name='views',
            field=models.IntegerField(),
        ),
    ]
