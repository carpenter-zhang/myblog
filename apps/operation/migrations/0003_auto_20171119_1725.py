# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 17:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acticle', '0001_initial'),
        ('operation', '0002_auto_20171119_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publish',
            options={'verbose_name': '发表文章', 'verbose_name_plural': '发表文章'},
        ),
        migrations.AddField(
            model_name='publish',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AddField(
            model_name='publish',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='acticle.Article', verbose_name='文章'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='acticle.Article', verbose_name='被评论文章'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default='', verbose_name='内容'),
        ),
    ]