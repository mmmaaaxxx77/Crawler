# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20151211_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='authorIntroduction',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='bookIntroduction',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='bookUrl',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='catalog',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='classification',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='collection',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='coverImageId',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='coverImageUrl',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='fromWhere',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='name2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='preface',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='specification',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='translator',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
