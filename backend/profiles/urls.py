from django.urls import path

from . import views

urlpatterns = [
    path("<slug:slug>/", views.ProfileDetail.as_view(), name="profile-detail"),
    # path("update/<int:pk>/", views.ProfileUpdateView.as_view()),
    # path("update/avatar/<int:pk>/", views.AvatarProfileUpdateView.as_view()),
]