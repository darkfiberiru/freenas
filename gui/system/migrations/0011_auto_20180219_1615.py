# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-19 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_syscons_to_vt'),
    ]

    operations = [
        migrations.AddField(
            model_name='advanced',
            name='adv_sed_user',
            field=models.CharField(choices=[('user', 'User'), ('master', 'Master')], default='user', help_text='User passed to camcontrol security -U for unlocking SEDs', max_length=120, verbose_name='camcontrol security user'),
        ),
    ]
