# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-26 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Solicitudes', '0010_auto_20180526_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='resolucion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='solucion',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
