# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-11 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='creation date', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='edition date', null=True, verbose_name='updated at')),
                ('name', models.CharField(help_text='The name of the commune', max_length=100, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name_plural': 'communes',
                'verbose_name': 'commune',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='creation date', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='edition date', null=True, verbose_name='updated at')),
                ('name', models.CharField(help_text='The name of the region', max_length=100, unique=True, verbose_name='name')),
                ('short_name', models.CharField(blank=True, help_text='A short name of the region', max_length=100, null=True, unique=True, verbose_name='short name')),
                ('order', models.PositiveIntegerField(blank=True, null=True)),
                ('importance', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'regions',
                'verbose_name': 'region',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='commune',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regions.Region'),
        ),
    ]