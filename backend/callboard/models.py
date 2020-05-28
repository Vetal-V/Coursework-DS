from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

from backend.units.transliteration import transliteration_ua_eng


class Category(MPTTModel):
    """Категорії оголошень"""
    name = models.CharField("Iм'я", max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name="Підкатегорія до:"
    )
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    # class MPTTMeta:
    class Meta:
        # order_insertion_by = ['name']
        verbose_name = "Категорій"
        verbose_name_plural = "Категорії"


class FilterAdvert(models.Model):
    """Фільтри"""
    name = models.CharField("Ім'я", max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фільтр"
        verbose_name_plural = "Фільтри"


class DateAdvert(models.Model):
    """Срок для обоголошення"""
    name = models.CharField("Ім'я", max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Срок"
        verbose_name_plural = "Сроки"
        ordering = ["id"]


class Advert(models.Model):
    """Оголошення"""
    user = models.ForeignKey(User, verbose_name="Користувач", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Категорія", on_delete=models.CASCADE)
    filters = models.ForeignKey(FilterAdvert, verbose_name="Фільтр", on_delete=models.CASCADE)
    date = models.ForeignKey(DateAdvert, verbose_name="Срок", on_delete=models.CASCADE)
    subject = models.CharField("Тема", max_length=200)
    description = models.TextField("Оголошення", max_length=10000)
    images = models.ForeignKey(
        'gallery.Gallery',
        verbose_name="Галерея фото",
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    file = models.FileField("Файл", upload_to="callboard_file/", blank=True, null=True)
    price = models.DecimalField("Ціна", max_digits=15, decimal_places=0)
    created = models.DateTimeField("Дата створення", auto_now_add=True)
    moderation = models.BooleanField("Модерація", default=False)
    slug = models.SlugField("url", max_length=200, unique=True)

    # def save(self, *args, **kwargs):
    #     self.slug = transliteration_ua_eng(self.subject) + "_" + str(self.id)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("advert-detail", kwargs={"category": self.category.slug, "slug": self.slug})

    class Meta:
        verbose_name = "Оголошення"
        verbose_name_plural = "Оголошення"