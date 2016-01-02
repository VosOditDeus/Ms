from django.contrib import admin
from photo.models import Album, Image, Tag

class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "images",'rating','public']
    empty_value_display = '-empty-'

class ImageAdmin(admin.ModelAdmin):
    # search_fields = ["title"]
    list_display = ["title", "user", "size", "tags_",'approved',
                    "created", 'thumbnail']
    list_filter = ["tags", "albums"]
    exclude = ['likes', 'liked_persons', 'thumbnail2']
    empty_value_display = '-empty-'
admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag)
admin.site.register(Image, ImageAdmin)