from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name='title', max_length=100)
    description_short = models.TextField(verbose_name='description_short')
    description_long = HTMLField(verbose_name='description_long')
    latitude = models.FloatField(verbose_name='latitude')
    longitude = models.FloatField(verbose_name='longitude')

    def __str__(self):
        return self.title


class Images(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Place', related_name='images', blank=True)
    image = models.ImageField(verbose_name='Image')
    position = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.position} {self.place}'
