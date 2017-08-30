# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asesores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='asesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='archivos_asesor', to='asesores.Asesor'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='asesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cita_asesor', to='asesores.Asesor'),
        ),
        migrations.AlterField(
            model_name='clave',
            name='asesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clave_asesor', to='asesores.Asesor'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='asesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='curso_asesor', to='asesores.Asesor'),
        ),
    ]
