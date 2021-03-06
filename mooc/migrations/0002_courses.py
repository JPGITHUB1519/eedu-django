# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('slogan', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('timeline', models.IntegerField(default=0)),
                ('released_date', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
