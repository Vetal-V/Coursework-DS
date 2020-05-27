from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Профіль користувача"""
    list_display = ("user", "first_name", "last_name", "phone", "email_two")
    search_fields = ("user", "first_name", "last_name", "phone", "email_two")
    prepopulated_fields = {"slug": ("first_name", "user")}