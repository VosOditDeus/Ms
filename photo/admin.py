from django.contrib import admin
from photo.models import Album, Image, Tag


class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "images"]


class ImageAdmin(admin.ModelAdmin):
    # search_fields = ["title"]
    list_display = ["__unicode__", "title", "user", "size", "tags_", "rating",
                    "created", 'thumbnail']
    list_filter = ["tags", "albums"]



admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag)
admin.site.register(Image, ImageAdmin)
