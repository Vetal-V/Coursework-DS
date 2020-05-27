from rest_framework import generics
from rest_framework import permissions
from django.views.generic import ListView, DetailView
from .models import Advert
# from .serializers import AdvertListSer, AdvertDetailSer, AdvertCreateSer


class AdvertList(ListView):
    """Всі оголошення"""
    # permission_classes = [permissions.AllowAny]
    model = Advert
    queryset = Advert.objects.all()
    template_name = "callboard/advert-list.html"
    # serializer_class = AdvertListSer


class AdvertDetail(DetailView):
    """Деталі оголошення"""
    # permission_classes = [permissions.AllowAny]
    model = Advert
    context_object_name = "advert"
    template_name = "callboard/advert-detail.html"
    # lookup_field = 'slug'
    # serializer_class = AdvertDetailSer