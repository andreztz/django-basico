# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrega', '0006_auto_20150917_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='partida',
            field=models.TimeField(null=True),
        ),
    ]
