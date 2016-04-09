# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(max_length=50, blank=True)),
                ('sity', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100, blank=True)),
                ('telephone', models.CharField(max_length=100, blank=True)),
                ('email', models.EmailField(max_length=100, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='person',
            field=models.ForeignKey(blank=True, to='Myapp.Person', null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='person',
            field=models.ManyToManyField(to='Myapp.Person'),
        ),
    ]
