from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название покемона')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='Английское название покемона')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='Японское название покемона')
    image = models.ImageField(upload_to='', verbose_name='Изображение покемона')
    description = models.TextField(blank=True, verbose_name='Описание покемона')
    previous_evolution = models.ForeignKey(
        'self', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='next_evolutions',
        verbose_name="Из какого покемона эволюционировал"
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Время появления')
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения')
    level = models.IntegerField(blank=True, verbose_name='Уровень')
    health = models.IntegerField(blank=True, verbose_name='Здоровье')
    Strength = models.IntegerField(blank=True, verbose_name='Сила')
    Defence = models.IntegerField(blank=True, verbose_name='Защита')
    Stamina = models.IntegerField(blank=True, verbose_name='Выносливость')

    def __str__(self):
        return f'{self.pokemon.title} - {self.id}'