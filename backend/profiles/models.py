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
    email_two = models.EmailField("Додатковий email")
    #TODO: change tp django-phone-field
    phone = models.CharField("Телефон", max_length=25)
    first_name = models.CharField("Ім'я", max_length=50)
    last_name = models.CharField("Прізвище", max_length=50, blank=True, null=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.first_name

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.slug = "{}{}".format(self.user_id, self.first_name)

    # def get_absolute_url(self):
    #     return reverse("profile-detail", kwargs={"slug": self.user.username})

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

