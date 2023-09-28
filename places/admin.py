from django.contrib import admin
from places.models import Place, Images


@admin.register(Images)
class AdminImages(admin.ModelAdmin):
    raw_id_fields = ['place', ]


class ImageInline(admin.TabularInline):
    model = Images


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
