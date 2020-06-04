from django.urls import path
from . import views


urlpatterns = [
    path("", views.SearchAdvert.as_view())
]
