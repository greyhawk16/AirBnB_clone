# Generated by Django 4.2.3 on 2023-07-21 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_rename_prices_per_night_house_prices_per_night'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='pets_allowed',
            field=models.BooleanField(default=True),
        ),
    ]