# Generated by Django 4.2.3 on 2023-07-21 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_rename_price_house_prices_per_night'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='priceS_per_night',
            new_name='prices_per_night',
        ),
    ]