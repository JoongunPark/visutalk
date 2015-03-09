# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserKakaoAuth',
            fields=[
                ('id', models.IntegerField(max_length=11, serialize=False, primary_key=True)),
                ('provider', models.CharField(max_length=32)),
                ('uid', models.CharField(unique=True, max_length=255)),
                ('user_id', models.IntegerField(max_length=11)),
                ('extra_data', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
