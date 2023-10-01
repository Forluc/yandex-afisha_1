from django.contrib import admin
from places.models import Place, Images
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase

SIZE_IMAGE = 200


class ImageInline(SortableAdminBase, admin.TabularInline):
    model = Images
    readonly_fields = ('show_preview',)

    def show_preview(self, obj):
        return format_html(
            '<img src="{}" width="{}">', obj.image.url, SIZE_IMAGE
        )


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
