from rest_framework import serializers

from .models import *


class PhotoSer(serializers.ModelSerializer):
    """Для виводу зображень"""

    class Meta:
        model = Photo
        fields = ("image",)


class GallerySer(serializers.ModelSerializer):
    """Для виводу галереї"""
    photos = PhotoSer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = ("photos",)