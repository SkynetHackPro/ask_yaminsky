# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-11 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0006_auto_20170411_1558'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='ask',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='tag',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='ask',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='asks', to='ask.Tag', verbose_name='Tags'),
        ),
    ]