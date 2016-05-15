# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name=b'Title')),
                ('content', models.CharField(max_length=10000, verbose_name=b'Content')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name=b'Updated Date')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]
