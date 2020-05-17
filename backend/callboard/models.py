from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    """Категорії оголошень"""
    name = models.CharField("Ім'я", max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name="Батьківський"
    )
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name = "Категорія"