# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-06-11 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='decsription',
            field=models.TextField(max_length=255),
        ),
    ]
