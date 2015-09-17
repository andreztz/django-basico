# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('fone', models.CharField(max_length=16, db_index=True)),
                ('ramal', models.CharField(blank=True, max_length=4, db_index=True)),
                ('contato', models.CharField(max_length=64, db_index=True)),
                ('outros_contatos', models.TextField(blank=True)),
                ('logradouro', models.CharField(max_length=32)),
                ('numero', models.PositiveIntegerField(verbose_name='número')),
                ('complemento', models.CharField(blank=True, max_length=32)),
                ('obs', models.TextField(blank=True)),
            ],
        ),
    ]
