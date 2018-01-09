# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-08 12:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='HaribhaktDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baps_type', models.CharField(choices=[('HB', 'Haribhakt'), ('SK', 'Sampark Karyakar'), ('MS', 'Mandal Sanchalak'), ('NI', 'Nirikshak'), ('ND', 'Nirdeshak')], default='HB', max_length=255)),
                ('name', models.CharField(max_length=250)),
                ('mobile_no', models.IntegerField(blank=True, max_length=10)),
                ('address', models.CharField(blank=True, max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='KaryakarGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('karyakar_to', models.DateField(auto_created=True)),
                ('karyakar_from', models.DateField(auto_created=True)),
                ('group_id', models.IntegerField(max_length=3)),
                ('haribhakt', models.ManyToManyField(related_name='haribhakt', to='attendance.HaribhaktDetail')),
                ('karyakar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='karyakar', to='attendance.HaribhaktDetail')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
