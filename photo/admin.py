from django.contrib import admin
from photo.models import Album, Image

class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "images",'rating','public']
    empty_value_display = '-empty-'

class ImageAdmin(admin.ModelAdmin):
    # search_fields = ["title"]
    list_display = ["title", "user", "size",'approved',
                    "created", 'thumbnail','tags_']
    list_filter = ["albums"]
    exclude = ['likes', 'liked_persons', 'thumbnail2']
    empty_value_display = '-empty-'
admin.site.register(Album, AlbumAdmin)
admin.site.register(Image, ImageAdmin)