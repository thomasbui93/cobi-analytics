# Generated by Django 2.2 on 2019-04-28 15:34

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics_schema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyticsschema',
            name='schema',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
