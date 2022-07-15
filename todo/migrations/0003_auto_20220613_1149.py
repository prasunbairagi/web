# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-06-13 06:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20220611_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='decsription',
        ),
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]