# Generated by Django 5.0 on 2023-12-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0017_episodio_vizualizacoes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
    ]
