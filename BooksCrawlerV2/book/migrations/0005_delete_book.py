# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20151211_0826'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
