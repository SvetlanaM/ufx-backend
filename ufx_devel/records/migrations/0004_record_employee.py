# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-15 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('records', '0003_auto_20170911_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.Employee'),
        ),
    ]
