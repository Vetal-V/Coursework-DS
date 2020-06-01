from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


def get_path_upload_avatar(instance,file):
    """
    make path of uploaded file shorter and return it
    in following format: (media)/profile_pics/user_1/myphoto_2018-12-2.png
    """
    time = timezone.now().strftime("%Y-%m-%d")
    end_extention = file.split('.')[-1]
    head = file.split('.')[0]
    if len(head) >10:
        head = head[:10]
    file_name =  head + '_' + time + '.' + end_extention
    return os.path.join('profile_pics','user_{0},{1}').format(instance.user.id,file_name)


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
    slug = models.SlugField("URL", max_length=50, default='')

    def __str__(self):
        return "{}".format(self.user)

    # def save(self, *args, **kwargs):
    #     self.slug = transliteration_ua_eng(self.login)
    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Профіль"
        verbose_name_plural = "Профілі"

    @property
    def get_avatar_url(self):
        if self.avatar:
            return '/media/{}'.format(self.avatar)
        else:
            return '/frontend/callboard-front/public/default-avatar.png'

    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            print("avatar detected")
            img = Image.open(self.avatar.path)
            if img.height > 150 or img.width > 150:
                output_size = (150,150)
                img.thumbnail(output_size)
                img.save(self.avatar.path)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Створення профілю користувача при реєстрації"""
    if created:
        Profile.objects.create(user=instance)


@receiver
def save_user_profile(sender, instance, **kwargs):
    """Зберегти профіль користувача після реєстрації"""
    instance.profile.save()
