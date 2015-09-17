# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrega', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('obs', models.TextField(blank=True)),
                ('cliente', models.ForeignKey(to='entrega.Cliente')),
            ],
        ),
    ]
