# Generated by Django 5.1rc1 on 2024-08-04 06:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0019_cheat_post_cheat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('progress', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('duration', models.IntegerField()),
                ('grade', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='cheat',
        ),
        migrations.DeleteModel(
            name='Cheat',
        ),
    ]
