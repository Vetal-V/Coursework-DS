from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

# from backend.gallery.models import Photo

from .serializers import AddPhotoSer, AddGallerySer, UpdateGallerySer
from .models import Photo
from .models import Gallery


class AddPhoto(generics.CreateAPIView):
    """Загрузити фото"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Photo.objects.all()
    serializer_class = AddPhotoSer


class AddGallery(generics.CreateAPIView):
    """Створити галерею"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Gallery.objects.all()
    serializer_class = AddGallerySer


class UpdateGallery(generics.UpdateAPIView):
    """Оновити галерею"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Gallery.objects.all()
    serializer_class = UpdateGallerySer
