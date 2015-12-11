# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('isbn', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('name2', models.CharField(max_length=255, blank=True)),
                ('author', models.CharField(max_length=255)),
                ('author2', models.CharField(max_length=255, blank=True)),
                ('translator', models.CharField(max_length=255, blank=True)),
                ('publisher', models.CharField(max_length=255, blank=True)),
                ('publicationDate', models.DateField()),
                ('language', models.CharField(max_length=255, blank=True)),
                ('collection', models.CharField(max_length=255, blank=True)),
                ('specification', models.CharField(max_length=255, blank=True)),
                ('publication', models.CharField(max_length=255, blank=True)),
                ('classification', models.CharField(max_length=255, blank=True)),
                ('coverImageId', models.CharField(max_length=255, blank=True)),
                ('coverImageUrl', models.URLField(blank=True)),
                ('bookUrl', models.URLField(blank=True)),
                ('bookIntroduction', models.TextField(blank=True)),
                ('authorIntroduction', models.TextField(blank=True)),
                ('catalog', models.TextField(blank=True)),
                ('preface', models.TextField(blank=True)),
                ('fromWhere', models.CharField(max_length=255, blank=True)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
