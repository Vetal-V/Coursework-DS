from django.urls import path

from . import views

urlpatterns = [
    path("upload/", views.AddPhoto.as_view()),
    path("creategallery/", views.AddGallery.as_view()),
    path("updategallery/<int:pk>/", views.UpdateGallery.as_view()),
]
