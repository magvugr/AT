# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 10:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppAdiccionTic', '0005_auto_20160817_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cancion',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Cancion',
        ),
    ]