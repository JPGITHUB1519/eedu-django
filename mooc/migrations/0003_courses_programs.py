# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0002_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='programs',
            field=models.ManyToManyField(to='mooc.Programs'),
        ),
    ]
