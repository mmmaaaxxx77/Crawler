# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name2',
            field=models.CharField(max_length=255),
        ),
    ]
