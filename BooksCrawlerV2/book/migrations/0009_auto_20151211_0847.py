# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_auto_20151211_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publicationDate',
            field=models.DateField(null=True),
        ),
    ]
