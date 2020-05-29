from rest_framework import generics
from rest_framework import permissions
from django.views.generic import ListView, DetailView
from .models import Advert
from .serializers import AdvertListSer, AdvertDetailSer, AdvertCreateSer


class AdvertList(generics.ListAPIView):
    """Всі оголошення"""
    permission_classes = [permissions.AllowAny]
    queryset = Advert.objects.all()
    serializer_class = AdvertListSer


class AdvertDetail(generics.RetrieveAPIView):
    """Деталі оголошення"""
    permission_classes = [permissions.AllowAny]
    queryset = Advert.objects.all()
    lookup_field = 'slug'
    serializer_class = AdvertDetailSer


class AdvertCreate(generics.CreateAPIView):
    """Добавлення оголошення"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Advert.objects.all()
    serializer_class = AdvertCreateSer