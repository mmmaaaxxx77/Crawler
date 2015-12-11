# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_remove_book_fromwhere_z'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='book',
            table='books',
        ),
    ]
