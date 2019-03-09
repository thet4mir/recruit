# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-19 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_auto_20190214_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='copy',
            field=models.FileField(blank=True, null=True, upload_to='person/document/'),
        ),
        migrations.AlterField(
            model_name='general',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='person/avatar/'),
        ),
    ]
