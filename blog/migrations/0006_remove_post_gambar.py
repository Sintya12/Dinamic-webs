# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-07 03:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_gambar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='gambar',
        ),
    ]
