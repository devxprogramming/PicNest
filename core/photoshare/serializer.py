from rest_framework import serializers
from .models import Album, Photo, Tag, ShareLink


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'slug')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
        read_only_fields = ('uploaded_at',)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ('slug',)

class ShareLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareLink
        fields = '__all__'
        read_only_fields = ('created_at', 'expires_at', 'link')
        # extra_kwargs = {
        #     'link': {'read_only': True},
        #     'photo': {'write_only': True}  # Make photo write-only to prevent exposure in API responses
        # }