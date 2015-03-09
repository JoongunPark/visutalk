# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visutalk', '0003_remove_userkakaoauth_extra_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='userkakaoauth',
            name='extra_data',
            field=models.CharField(max_length=150, blank=True),
            preserve_default=True,
        ),
    ]
