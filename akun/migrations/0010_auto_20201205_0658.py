# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-05 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akun', '0009_auto_20201205_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='tentang',
            field=models.TextField(blank=True, default='silahkan deskripsikan tentang diri anda', max_length=100),
        ),
    ]
