from django.contrib import admin
from .models import Album,Song,Artist

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
