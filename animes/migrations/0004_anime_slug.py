# Generated by Django 5.0 on 2023-12-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0003_episodio_postado_em'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
