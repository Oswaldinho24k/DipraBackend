# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-01 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20170818_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='asesorId',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='clienteId',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
