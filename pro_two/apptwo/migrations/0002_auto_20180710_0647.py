# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-10 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptwo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=264, unique=True),
        ),
    ]