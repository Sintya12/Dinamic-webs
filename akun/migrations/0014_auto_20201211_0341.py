# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-11 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akun', '0013_profil_nama_lengkap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='gambar',
            field=models.ImageField(blank=True, default='default.jpeg', upload_to='profil_img'),
        ),
    ]
