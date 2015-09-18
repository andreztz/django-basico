# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrega', '0007_auto_20150917_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='fidelidade',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='entregador',
            field=models.ForeignKey(null=True, to='entrega.Entregador', blank=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='partida',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
