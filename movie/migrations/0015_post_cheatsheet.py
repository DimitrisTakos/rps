# Generated by Django 5.1rc1 on 2024-07-28 23:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0014_cheatsheet_remove_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cheatsheet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.cheatsheet'),
        ),
    ]
