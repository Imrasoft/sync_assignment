# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sync', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=100, null=True)),
                ('urn', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField()),
                ('complete_runs', models.IntegerField(default=0)),
                ('interrupted_runs', models.IntegerField(default=0)),
                ('expired_runs', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_id', models.IntegerField(default=0)),
                ('responded', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(null=True)),
                ('modified_on', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
                ('run_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sync.Run')),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
                ('run_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sync.Run')),
            ],
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.AddField(
            model_name='flow',
            name='run_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sync.Run'),
        ),
    ]