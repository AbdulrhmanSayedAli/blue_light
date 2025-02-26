# Generated by Django 4.2.17 on 2025-01-13 19:17

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_historicaluser_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
    ]
