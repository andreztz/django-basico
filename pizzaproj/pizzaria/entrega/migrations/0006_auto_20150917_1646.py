# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrega', '0005_auto_20150917_1551'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entregador',
            options={'verbose_name_plural': 'Entregadores'},
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='data_hora',
            new_name='entrada',
        ),
        migrations.AddField(
            model_name='pedido',
            name='partida',
            field=models.DateTimeField(null=True),
        ),
    ]
