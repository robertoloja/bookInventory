# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-18 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20160217_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='comments',
            field=models.TextField(blank=True),
        ),
    ]
