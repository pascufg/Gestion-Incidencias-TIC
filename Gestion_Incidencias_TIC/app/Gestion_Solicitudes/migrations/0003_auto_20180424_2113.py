# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-24 19:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Solicitudes', '0002_auto_20180424_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitud',
            old_name='ci',
            new_name='CI',
        ),
    ]