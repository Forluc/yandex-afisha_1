from adminsortable2.admin import SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from places.models import Image, Place

IMAGE_HEIGHT = 200
IMAGE_WIDTH = 200


class ImageInline(SortableAdminBase, admin.TabularInline):
    model = Image
    readonly_fields = ('show_preview',)

    def show_preview(self, obj):
        return format_html(
            '<img src="{}" width="{}" height ="{}">', obj.image.url, IMAGE_WIDTH, IMAGE_HEIGHT
        )


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    raw_id_fields = ('place', )


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    search_fields = ['title', ]
    inlines = [
        ImageInline,
    ]
