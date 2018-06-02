# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-30 16:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Gestion_Alumnos', '0011_auto_20180527_1331'),
        ('Gestion_Centros', '0015_tema_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('registro', models.DateTimeField(auto_now_add=True)),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('foto', models.ImageField(blank=True, upload_to='post_image')),
                ('centro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gestion_Centros.Centro')),
                ('equipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gestion_Alumnos.Equipo')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
