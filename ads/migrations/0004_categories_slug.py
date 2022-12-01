# Generated by Django 4.1.3 on 2022-12-01 11:30

import ads.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_selection'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.CharField(max_length=10, null=True, unique=True, validators=[ads.models.check_min_categories_slug]),
        ),
    ]
