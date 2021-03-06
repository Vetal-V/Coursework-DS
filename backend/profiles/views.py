from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from backend.callboard.models import Advert
from backend.callboard.serializers import AdvertListSer, AdvertCreateSer, AdvertCreateSer

from .serializers import ProfileSer, ProfileUpdateSer, AvatarUpdateSer
from .models import Profile


class ProfileDetail(generics.RetrieveAPIView):
    """Профіль користувача"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSer
    queryset = Profile.objects.all()
    # def get_queryset(self):
    #     return Advert.objects.filter(user=self.request.user)


class ProfileUpdateView(generics.UpdateAPIView):
    """Редагувати профіль користувача"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSer


class UserAdvertList(generics.ListAPIView):
    """Всі оголошення користувача"""
    permission_classes = [permissions.IsAuthenticated]
    # serializer_class = AdvertListSer
    #
    # def get_queryset(self):
    #     return Advert.objects.filter(user=self.request.user)
    def get(self, request):
        adverts = Advert.objects.filter(user=request.user)
        ser = AdvertListSer(adverts, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = AdvertCreateSer(data=request.data)
        print(request.data.get("id"))
        if ser.is_valid():
            if request.data.get("id"):
                ser.save(parent_id=request.data.get("id"), user=request.user)
            else:
                ser.save(user=request.user)
            return Response(status=200)
        else:
            return Response(status=400)


class UserAdvertUpdate(generics.UpdateAPIView):
    """Редагування оголошень користувачів"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AdvertCreateSer

    def get_queryset(self):
        return Advert.objects.filter(user=self.request.user)


class AvatarProfileUpdateView(generics.UpdateAPIView):
    """Редагування аватара користувача"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = AvatarUpdateSer
