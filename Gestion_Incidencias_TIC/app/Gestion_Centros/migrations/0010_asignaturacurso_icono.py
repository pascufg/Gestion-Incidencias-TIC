# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-27 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Centros', '0009_asignatura_asignaturacurso'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignaturacurso',
            name='icono',
            field=models.ImageField(blank=True, upload_to='post_image'),
        ),
    ]