# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-09 12:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='haribhaktdetail',
            name='mobile_no',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='haribhaktdetail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='karyakargroup',
            name='group_id',
            field=models.IntegerField(),
        ),
    ]
