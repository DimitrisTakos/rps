# Generated by Django 5.1rc1 on 2024-08-04 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0017_remove_post_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='progress',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
