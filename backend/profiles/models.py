from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    """Модель профілю користувача"""
    user = models.OneToOneField(User, verbose_name="Користувач", on_delete=models.CASCADE)
    #TODO change to media
    avatar = models.ImageField("Фото профілю", upload_to="profile/", blank=True, null=True)
    #TODO: change tp django-phone-field
    phone = models.CharField("Телефон", max_length=25)
    first_name = models.CharField("Ім'я", max_length=50)
    last_name = models.CharField("Прізвище", max_length=50, default="", blank=True, null=True)
    #TODO: set unnecessary
    email_two = models.EmailField("Додатковий email", max_length=50, default=" ")
    slug = models.SlugField("url", max_length=200, unique=True, default='')
    # slug = models.SlugField("URL", max_length=50, default='')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Профіль"
        verbose_name_plural = "Профілі"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Створення профілю користувача при реєстрації"""
    if created:
        Profile.objects.create(user=instance)


@receiver
def save_user_profile(sender, instance, **kwargs):
    """Зберегти профіль користувача після реєстрації"""
    instance.profile.save()

