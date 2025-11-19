from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'caption', 'keywords', 'date')
    search_fields = ('caption', 'keywords')
