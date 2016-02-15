# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(blank=True)),
                ('api_document', models.CharField(max_length=1000, null=True, blank=True)),
                ('status', models.IntegerField(default=1, blank=True)),
            ],
        ),
    ]
