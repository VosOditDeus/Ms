from django.contrib import admin
from photo.models import  Image,Categories
class ImageAdmin(admin.ModelAdmin):
    # search_fields = ["title"]
    list_display = ["title", "user",'approved',
                    "created", 'tags_','thumbnail']
    exclude = ['likes', 'liked_persons']
    empty_value_display = '-empty-'
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_images']
    empty_value_display= '-empty-'
admin.site.register(Image, ImageAdmin)
admin.site.register(Categories, CategoriesAdmin)