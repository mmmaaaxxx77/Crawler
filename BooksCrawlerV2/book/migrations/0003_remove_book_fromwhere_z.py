# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_fromwhere_z'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='fromWhere_z',
        ),
    ]
