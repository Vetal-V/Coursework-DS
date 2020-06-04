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


class AddPhotoSer(serializers.ModelSerializer):
    """Для додавання фото"""
    class Meta:
        model = Photo
        fields = ("image", "name")


class AddGallerySer(serializers.ModelSerializer):
    """Для створення галереї з завантажених фото"""
    photos = PhotoSer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = ("name", "photos")


class UpdateGallerySer(serializers.ModelSerializer):
    """Для добавлення фото в галерею"""
    # photos = PhotoSer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = ("name", "photos")
