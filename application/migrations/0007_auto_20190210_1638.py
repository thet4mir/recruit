# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-10 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_auto_20190125_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='copy',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='general',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]