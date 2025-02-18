from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название категории
    slug = models.SlugField(unique=True)  # SEO-URL категории

    def __str__(self):
        return self.name


class ProductType(models.Model):  # Тип продутов. (например, категория: "Монитор", product type (тип) "Игровые" и т. д.)
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


