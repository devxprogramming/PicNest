from django.contrib import admin
from .models import Photo, Album, ShareLink, Tag


# Register your models here.
class ShareLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'created_at', 'expires_at', 'permissions')
    search_fields = ('photo__title', 'photo__album__title')
    list_filter = ('permissions', 'created_at', 'expires_at')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'album', 'uploader', 'uploaded_at')
    search_fields = ('title', 'album__title', 'uploader__username')
    # list_filter = ('album', 'uploader', 'uploaded_at')
    # # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('album', 'uploader')

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'created_at', 'is_public', 'is_favorite')
    search_fields = ('title', 'owner__username')
    # list_filter = ('is_public', 'is_favorite', 'created_at')
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('owner',)
    # readonly_fields = ('created_at', 'updated_at')

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    # search_fields = ('name',)
    # prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(ShareLink, ShareLinkAdmin)
admin.site.register(Tag, TagAdmin)