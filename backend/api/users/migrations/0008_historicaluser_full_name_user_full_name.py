# Generated by Django 4.2.17 on 2025-01-20 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_historicaluniveristy_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='full_name',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='', max_length=300),
        ),
    ]