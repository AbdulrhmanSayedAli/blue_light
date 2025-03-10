# Generated by Django 4.2.17 on 2025-02-04 17:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0007_alter_file_info_alter_file_pages_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='favourite_users',
            field=models.ManyToManyField(related_name='favourite_courses', to=settings.AUTH_USER_MODEL),
        ),
    ]
