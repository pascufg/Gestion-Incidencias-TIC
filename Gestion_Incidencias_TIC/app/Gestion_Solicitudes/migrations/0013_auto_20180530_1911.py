# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-30 17:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Solicitudes', '0012_auto_20180526_1344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actividad',
            old_name='usuarioAsignado',
            new_name='usuario',
        ),
    ]