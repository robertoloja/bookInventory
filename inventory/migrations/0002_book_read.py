# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
