# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_certification_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='skill',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
    ]