# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-05 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akun', '0005_auto_20201205_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='hp',
            field=models.IntegerField(blank=True, default=62),
        ),
    ]
