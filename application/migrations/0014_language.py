# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-24 04:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0013_auto_20190222_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(choices=[('', 'Сонгох'), ('english', 'Англи хэл'), ('russian', 'Орос хэл'), ('chinesse', 'Хятад хэл'), ('korean', 'Солонгос хэл'), ('japanesse', 'Япон'), ('spanish', 'Испани'), ('other', 'Бусад')], default='Сонгох', max_length=16)),
                ('writing', models.CharField(choices=[('', 'Сонгох'), ('unacceptable', '1-Муу'), ('below_average', '2-Дундаас доош'), ('average', '3-Дунд'), ('above_average', '4-Сайн'), ('excellent', '5-Маш сайн')], default='Сонгох', max_length=16)),
                ('reading', models.CharField(choices=[('', 'Сонгох'), ('unacceptable', '1-Муу'), ('below_average', '2-Дундаас доош'), ('average', '3-Дунд'), ('above_average', '4-Сайн'), ('excellent', '5-Маш сайн')], default='Сонгох', max_length=16)),
                ('speaking', models.CharField(choices=[('', 'Сонгох'), ('unacceptable', '1-Муу'), ('below_average', '2-Дундаас доош'), ('average', '3-Дунд'), ('above_average', '4-Сайн'), ('excellent', '5-Маш сайн')], default='Сонгох', max_length=16)),
                ('listening', models.CharField(choices=[('', 'Сонгох'), ('unacceptable', '1-Муу'), ('below_average', '2-Дундаас доош'), ('average', '3-Дунд'), ('above_average', '4-Сайн'), ('excellent', '5-Маш сайн')], default='Сонгох', max_length=16)),
                ('general', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='language', to='application.General')),
            ],
        ),
    ]