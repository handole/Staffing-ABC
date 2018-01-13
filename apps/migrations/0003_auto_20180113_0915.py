# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-13 09:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20180113_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiter',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='uploadresume',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]