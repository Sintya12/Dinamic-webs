# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-04 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akun', '0003_auto_20201204_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='Hp',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='profil',
            name='alamat',
            field=models.TextField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profil',
            name='tentang',
            field=models.TextField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profil',
            name='website',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
