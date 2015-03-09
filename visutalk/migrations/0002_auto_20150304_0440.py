# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visutalk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userkakaoauth',
            name='id',
            field=models.AutoField(max_length=11, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
