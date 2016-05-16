# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_important',
            field=models.BooleanField(verbose_name='Important', default=False),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(max_length=10000, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
    ]
