from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name='title', max_length=100, unique=True)
    short_description = models.TextField(verbose_name='short_description', blank=True)
    long_description = HTMLField(verbose_name='long_description', blank=True)
    latitude = models.FloatField(verbose_name='latitude')
    longitude = models.FloatField(verbose_name='longitude')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Place', related_name='images')
    image = models.ImageField(verbose_name='Image')
    position = models.PositiveIntegerField(verbose_name='Position', db_index=True, default=0, blank=True)

    def __str__(self):
        return f'{self.position} {self.place}'

    class Meta:
        ordering = ['position']
