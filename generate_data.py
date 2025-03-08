from django.db import models
from django.utils.text import slugify  # Import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название категории
    slug = models.SlugField(unique=True, blank=True)  # SEO-URL категории, blank=True
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories'
    )  # Родительская категория (для подкатегорий)

    def __str__(self):
        return self.name if not self.parent else f"{self.parent.name} -> {self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it doesn't exist
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProductType(models.Model):  # Теперь это подкатегория
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_types")

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        verbose_name = "Тип продукта"
        verbose_name_plural = "Типы продуктов"