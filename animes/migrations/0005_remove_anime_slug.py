# Generated by Django 5.0 on 2023-12-12 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0004_anime_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='slug',
        ),
    ]
