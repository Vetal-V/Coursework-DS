from rest_framework import serializers

from backend.gallery.serializers import GallerySer
from backend.profiles.serializers import ProfileSer
from .models import *
# from backend.profiles.models import Profile

class UserSerialiser(serializers.ModelSerializer):
    """Серіалізація користувача"""
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "email",)


class CategorySer(serializers.ModelSerializer):
    """Для виводу категорій"""
    class Meta:
        model = Category
        fields = ("name", )


class FilterAdvertSer(serializers.ModelSerializer):
    """Для виводу фільтрів"""
    class Meta:
        model = FilterAdvert
        fields = ("name", )


class AdvertListSer(serializers.ModelSerializer):
    """Для виводу списку оголошень"""
    category = CategorySer()
    filters = FilterAdvertSer()
    images = GallerySer(read_only=True)
    user = UserSerialiser()


    class Meta:
        model = Advert
        fields = ("id", "user" ,"category", "filters", "subject", "images", "price", "created", "slug")


class AdvertDetailSer(serializers.ModelSerializer):
    """Для виводу повного оголошення"""
    category = CategorySer()
    filters = FilterAdvertSer()
    images = GallerySer(read_only=True)
    user= UserSerialiser()
    profile = ProfileSer(read_only=True, many=True)

    class Meta:
        model = Advert
        fields = (
            "user",
            "profile",
            "category",
            "filters",
            "subject",
            "description",
            "images",
            "file",
            "price",
            "created",
            "user"
        )

class AdvertCreateSer(serializers.ModelSerializer):
    """Добавлення оголошення"""
    class Meta:
        model = Advert
        fields = (
            "category",
            "filters",
            "date",
            "subject",
            "description",
            "price",
            "images"
        )

    def create(self, request):
        request["user"] = self.context['request'].user
        advert = Advert.objects.create(**request)
        return advert
