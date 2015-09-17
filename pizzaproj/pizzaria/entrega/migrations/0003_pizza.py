# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrega', '0002_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('sabor', models.CharField(max_length=32, choices=[('', '(escolha o sabor)'), ('mozzarella', 'Muçarela'), ('calabresa', 'Calabresa'), ('portuguesa', 'Portuguesa'), ('4queijos', '4 Queijos')])),
                ('sabor2', models.CharField(max_length=32, choices=[('', '(escolha o sabor)'), ('mozzarella', 'Muçarela'), ('calabresa', 'Calabresa'), ('portuguesa', 'Portuguesa'), ('4queijos', '4 Queijos')], blank=True)),
                ('obs', models.TextField(blank=True)),
                ('pedido', models.ForeignKey(to='entrega.Pedido')),
            ],
        ),
    ]
