# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-29 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='姓名')),
                ('phone', models.CharField(max_length=32, verbose_name='联系方式')),
                ('number', models.CharField(max_length=32, verbose_name='网吧代码')),
            ],
            options={
                'verbose_name': '报名信息',
                'verbose_name_plural': '报名信息',
            },
        ),
    ]
