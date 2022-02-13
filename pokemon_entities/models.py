from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    level = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    Strength = models.IntegerField(default=0)
    Defence = models.IntegerField(default=0)
    Stamina = models.IntegerField(default=0)