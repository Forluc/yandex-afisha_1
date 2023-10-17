from adminsortable2.admin import SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from places.models import Image, Place

SIZE_IMAGE = 200


class ImageInline(SortableAdminBase, admin.TabularInline):
    model = Image
    readonly_fields = ('show_preview',)

    def show_preview(self, obj):
        return format_html(
            '<img src="{}" width="{}">', obj.image.url, SIZE_IMAGE
        )


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    search_fields = ['title', ]
    inlines = [
        ImageInline,
    ]
