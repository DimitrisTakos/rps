# Generated by Django 5.1rc1 on 2024-08-05 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0023_post_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
