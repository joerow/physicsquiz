# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculationquestion',
            name='imagey',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
