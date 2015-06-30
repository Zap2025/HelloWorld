# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=40)),
                ('birthdate', models.DateField()),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
