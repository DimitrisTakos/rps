# Generated by Django 5.1rc1 on 2024-07-27 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_alter_videos_url'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Videos',
            new_name='Video',
        ),
    ]
