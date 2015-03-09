# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visutalk', '0002_auto_20150304_0440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userkakaoauth',
            name='extra_data',
        ),
    ]
