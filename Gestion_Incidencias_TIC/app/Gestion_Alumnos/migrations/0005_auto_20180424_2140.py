# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-24 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Alumnos', '0004_alumno_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='foto',
            field=models.ImageField(blank=True, upload_to='post_image'),
        ),
    ]
