# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-02 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Centros', '0018_centro_incidencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centro',
            name='incidencia',
            field=models.TextField(blank=True, max_length=120, null=True),
        ),
    ]