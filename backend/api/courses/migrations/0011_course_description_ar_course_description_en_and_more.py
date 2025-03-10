# Generated by Django 4.2.17 on 2025-02-24 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_alter_video_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='name_ar',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='name_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='coursegroup',
            name='name_ar',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='coursegroup',
            name='name_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='name_ar',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='name_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='historicalcourse',
            name='description_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='historicalcourse',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='historicalcourse',
            name='name_ar',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='historicalcourse',
            name='name_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='historicalcoursegroup',
            name='name_ar',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='historicalcoursegroup',
            name='name_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='historicalfile',
            name='name_ar',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='historicalfile',
            name='name_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='historicalquiz',
            name='name_ar',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='historicalquiz',
            name='name_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='historicalvideo',
            name='name_ar',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='historicalvideo',
            name='name_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='name_ar',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='name_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='name_ar',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='name_en',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
