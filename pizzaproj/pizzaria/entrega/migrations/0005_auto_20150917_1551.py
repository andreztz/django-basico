# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrega', '0004_auto_20150917_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entregador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='entregador',
            field=models.ForeignKey(null=True, to='entrega.Entregador'),
        ),
    ]
