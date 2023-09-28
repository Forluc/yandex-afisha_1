from django.contrib import admin
from places.models import Place, Images
from django.utils.html import format_html

SIZE_IMAGE = 200


@admin.register(Images)
class AdminImage(admin.ModelAdmin):
    raw_id_fields = ['place']
    readonly_fields = ['show_preview']

    def show_preview(self, obj):
        return format_html(
            '<img src="{}" width="{}">', obj.image.url, 200
        )


class ImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ['show_preview']

    def show_preview(self, obj):
        return format_html(
            '<img src="{}" width="{}">', obj.image.url, 200
        )


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
