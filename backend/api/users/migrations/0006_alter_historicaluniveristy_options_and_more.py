# Generated by Django 4.2.17 on 2025-01-14 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_historicaluser_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaluniveristy',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical univeristy', 'verbose_name_plural': 'historical Univeristies/'},
        ),
        migrations.AlterModelOptions(
            name='univeristy',
            options={'verbose_name_plural': 'Univeristies/'},
        ),
        migrations.AlterField(
            model_name='city',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cities/'),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='specializations/'),
        ),
        migrations.AlterField(
            model_name='univeristy',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='univeristies/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
    ]
