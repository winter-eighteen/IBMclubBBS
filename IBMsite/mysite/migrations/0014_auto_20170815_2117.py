# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_auto_20170815_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_model',
            name='department',
            field=models.CharField(choices=[('\u79d8\u4e66\u90e8', b'\xe7\xa7\x98\xe4\xb9\xa6\xe9\x83\xa8'), ('\u4eba\u529b\u8d44\u6e90\u90e8', b'\xe4\xba\xba\xe5\x8a\x9b\xe8\xb5\x84\xe6\xba\x90\xe9\x83\xa8'), ('\u5ba3\u4f20\u90e8', b'\xe5\xae\xa3\xe4\xbc\xa0\xe9\x83\xa8'), ('\u7ec4\u7ec7\u90e8', b'\xe7\xbb\x84\xe7\xbb\x87\xe9\x83\xa8'), ('\u4e3b\u5e2d', b'\xe4\xb8\xbb\xe5\xb8\xad'), ('\u79d8\u4e66\u90e8\u90e8\u957f', b'\xe7\xa7\x98\xe4\xb9\xa6\xe9\x83\xa8\xe9\x83\xa8\xe9\x95\xbf'), ('\u4eba\u529b\u8d44\u6e90\u90e8\u90e8\u957f', b'\xe4\xba\xba\xe5\x8a\x9b\xe8\xb5\x84\xe6\xba\x90\xe9\x83\xa8\xe9\x83\xa8\xe9\x95\xbf'), ('\u5ba3\u4f20\u90e8\u90e8\u957f', b'\xe5\xae\xa3\xe4\xbc\xa0\xe9\x83\xa8\xe9\x83\xa8\xe9\x95\xbf'), ('\u7ec4\u7ec7\u90e8\u90e8\u957f', b'\xe7\xbb\x84\xe7\xbb\x87\xe9\x83\xa8\xe9\x83\xa8\xe9\x95\xbf')], max_length=12, null=True),
        ),
    ]