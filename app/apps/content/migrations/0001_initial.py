# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(help_text=b'Used for URL. ', unique=True)),
            ],
            options={
                'ordering': ['-slug'],
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(help_text=b'Used for URL. ', unique=True)),
                ('description', models.CharField(help_text=b'Description of the Language.', max_length=255, verbose_name='description', blank=True)),
            ],
            options={
                'ordering': ['-slug'],
                'verbose_name_plural': 'languages',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(help_text=b'Used for URL. ', unique=True)),
                ('parent_category', models.ManyToManyField(to='content.Category', blank=True)),
            ],
            options={
                'ordering': ['-slug'],
                'verbose_name_plural': 'SubCategories',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='language',
            field=models.ManyToManyField(to='content.Language', null=True, blank=True),
        ),
    ]
