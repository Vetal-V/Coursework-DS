from rest_framework import generics
from rest_framework import permissions

from backend.callboard.models import Advert
from backend.callboard.serializers import AdvertListSer, AdvertCreateSer

from .serializers import ProfileSer, ProfileUpdateSer
from .models import Profile


class ProfileDetail(generics.RetrieveAPIView):
    """Профіль користувача"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSer


class ProfileUpdateView(generics.UpdateAPIView):
    """Редагувати профіль користувача"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSer


class UserAdvertList(generics.ListAPIView):
    """Всі оголошення користувача"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AdvertListSer

    def get_queryset(self):
        return Advert.objects.filter(user=self.request.user)


class UserAdvertUpdate(generics.UpdateAPIView):
    """Редагування оголошень користувачів"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AdvertCreateSer

    def get_queryset(self):
        return Advert.objects.filter(user=self.request.user)