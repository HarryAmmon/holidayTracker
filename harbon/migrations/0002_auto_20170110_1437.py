# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-10 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harbon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holidayrequest',
            name='UID',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='holidayrequest',
            name='approved',
            field=models.NullBooleanField(verbose_name=False),
        ),
    ]
