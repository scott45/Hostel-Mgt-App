# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Book_id', models.CharField(max_length=5, default='')),
                ('Booked_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('views', models.IntegerField(max_length=5)),
                ('likes', models.IntegerField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('Custodian', models.CharField(max_length=25, blank=True)),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('classification', models.ForeignKey(to='Gyobera.Classification')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Room_Number', models.CharField(max_length=50)),
                ('Total_rooms', models.IntegerField(blank=True)),
                ('Price_single', models.IntegerField(blank=True)),
                ('Price_double', models.IntegerField(blank=True)),
                ('Hostel', models.ForeignKey(to='Gyobera.List')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Names', models.CharField(max_length=100)),
                ('Sex', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])),
                ('Age', models.IntegerField()),
                ('Registration_Number', models.CharField(max_length=100)),
                ('Course', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='Booked_by',
            field=models.ForeignKey(to='Gyobera.Student', default=''),
        ),
        migrations.AddField(
            model_name='booking',
            name='Room_Number',
            field=models.ForeignKey(to='Gyobera.Room'),
        ),
    ]
