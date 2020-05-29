from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSer(serializers.ModelSerializer):
    """Серіалізація користувача"""
    class Meta:
        model = User
        fields = ("username", "email")


class ProfileSer(serializers.ModelSerializer):
    """Профіль користувача"""
    user = UserSer()

    class Meta:
        model = Profile
        fields = ("user", "avatar", "email_two", "phone", "first_name", "last_name")


class ProfileUpdateSer(serializers.ModelSerializer):
    """Редагування профілю користувача"""
    class Meta:
        model = Profile
        fields = ("avatar", "email_two", "phone", "first_name", "last_name")
