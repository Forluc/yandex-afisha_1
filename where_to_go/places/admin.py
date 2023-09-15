from django.contrib import admin
from .models import Place, Images


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass
