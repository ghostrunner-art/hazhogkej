# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-06 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhizhu_proxy', '0003_auto_20181031_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='number',
            field=models.CharField(default='003', max_length=32, verbose_name='网吧代码'),
        ),
    ]
