from django.views.generic import DetailView
from rest_framework import generics
from rest_framework import permissions

from .models import Profile


class ProfileDetail(DetailView):
    """Профиль пользователя"""
    # permission_classes = [permissions.IsAuthenticated]
    model = Profile
    context_object_name = "profile"
    template_name = "profiles/user-detail.html"
    # queryset = Profile.objects.all()

