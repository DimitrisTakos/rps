# Generated by Django 5.1rc1 on 2024-07-28 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0012_remove_post_zip_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(null=True, upload_to='cheatsheets/'),
        ),
    ]
