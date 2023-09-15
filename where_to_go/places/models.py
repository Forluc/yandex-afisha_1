from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name='title', max_length=100)
    description_short = models.TextField(verbose_name='description_short')
    description_long = models.TextField(verbose_name='description_long')
    latitude = models.FloatField(verbose_name='latitude')
    longitude = models.FloatField(verbose_name='longitude')

    def __str__(self):
        return self.title
