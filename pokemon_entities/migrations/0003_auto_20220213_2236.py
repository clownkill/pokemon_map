# Generated by Django 3.1.14 on 2022-02-13 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_auto_20220213_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='Defence',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='Stamina',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='Strength',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
