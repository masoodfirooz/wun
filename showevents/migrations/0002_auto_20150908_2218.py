# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showevents', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='location',
            new_name='locationAddress',
        ),
        migrations.AddField(
            model_name='event',
            name='locationLattitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='locationLongitude',
            field=models.FloatField(null=True),
        ),
    ]
