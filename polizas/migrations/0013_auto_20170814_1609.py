# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-14 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polizas', '0012_cliente_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='poliza',
            name='modalidad',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='poliza',
            name='subrama',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
