# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdDateTime', models.DateTimeField(auto_now_add=True)),
                ('startDateTime', models.DateTimeField()),
                ('endDateTime', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('userGoing', models.ForeignKey(related_name='userGoing', to=settings.AUTH_USER_MODEL)),
                ('userPosted', models.ForeignKey(related_name='userPosted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
