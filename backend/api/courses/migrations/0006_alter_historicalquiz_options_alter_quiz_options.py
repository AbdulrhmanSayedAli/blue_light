# Generated by Django 4.2.17 on 2025-01-19 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_historicalquiz_info_title_quiz_info_title_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalquiz',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical quiz', 'verbose_name_plural': 'historical Quizzes'},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name_plural': 'Quizzes'},
        ),
    ]