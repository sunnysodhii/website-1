# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-24 10:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0014_auto_20200824_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='networkgroup',
            name='position',
        ),
    ]
