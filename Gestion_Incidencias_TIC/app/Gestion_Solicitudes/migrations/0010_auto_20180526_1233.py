# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-26 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Solicitudes', '0009_actividad_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='solicitud',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gestion_Solicitudes.Solicitud'),
        ),
    ]