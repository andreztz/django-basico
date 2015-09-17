# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrega', '0003_pizza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='obs',
            field=models.CharField(max_length=256, blank=True),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='obs',
            field=models.CharField(max_length=256, blank=True),
        ),
    ]
