# Generated by Django 5.0 on 2023-12-12 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0006_anime_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
