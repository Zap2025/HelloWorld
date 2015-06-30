# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=75)),
                ('extension', models.IntegerField(blank=True)),
                ('office', models.CharField(max_length=20, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(blank=True, to='registrar.Professor', null=True),
            preserve_default=True,
        ),
    ]
