# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-03 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Solicitudes', '0016_auto_20180603_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='alumno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gestion_Alumnos.Alumno'),
        ),
    ]
