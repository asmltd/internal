# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-05 11:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Object', models.CharField(max_length=50)),
                ('Giventime', models.DateField()),
                ('ExpectedReturnTime', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Userdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('UserId', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Dob', models.DateField()),
                ('Doj', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='GivenTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppRestful.Userdetail'),
        ),
    ]
