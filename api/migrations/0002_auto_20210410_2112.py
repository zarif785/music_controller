# Generated by Django 3.1.5 on 2021-04-10 15:12

import api.api_models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=api.api_models.generate_unique_code, max_length=8, unique=True),
        ),
    ]
