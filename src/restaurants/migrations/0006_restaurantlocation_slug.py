# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-13 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20180309_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
