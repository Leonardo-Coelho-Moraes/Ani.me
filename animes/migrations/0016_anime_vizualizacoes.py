# Generated by Django 5.0 on 2023-12-17 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0015_alter_anime_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='vizualizacoes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
