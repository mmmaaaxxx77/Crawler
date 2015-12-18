# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_auto_20151211_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookUrl',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='coverImageUrl',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True),
        ),
    ]
