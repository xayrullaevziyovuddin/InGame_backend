from django.db import models
from .categories import Category, ProductType
from .brands import Brand
from attributes.models import Attribute


class Product(models.Model):
    """Модель товара (компьютера или комплектующего)"""
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="SEO-URL")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    discount_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Цена со скидкой"
    )
    stock = models.PositiveIntegerField(default=0, verbose_name="Количество на складе")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    # Связи с другими моделями
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категория"
    )
    product_type = models.ForeignKey(
        ProductType, on_delete=models.CASCADE, related_name="products", verbose_name="Тип продукта"
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name="products", verbose_name="Бренд"
    )
    attributes = models.ManyToManyField(
        Attribute, through="ProductAttribute", related_name="products", verbose_name="Характеристики"
    )

    # Изображения
    main_image = models.ImageField(upload_to="products/", verbose_name="Главное изображение")

    def get_discount_percentage(self):
        """Получение процента скидки, если она есть"""
        if self.discount_price and self.price > 0:
            discount = ((self.price - self.discount_price) / self.price) * 100
            return round(discount, 1)
        return 0

    def get_final_price(self):
        """Получение финальной цены (со скидкой, если есть)"""
        return self.discount_price if self.discount_price else self.price

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["price"]),
            models.Index(fields=["brand"]),
            models.Index(fields=["is_active"]),
        ]


class ProductAttribute(models.Model):
    """Связующая модель между продуктами и их характеристиками"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("product", "attribute")
        verbose_name = "Характеристика товара"
        verbose_name_plural = "Характеристики товаров"


class ProductImage(models.Model):
    """Дополнительные изображения товара"""
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images", verbose_name="Товар"
    )
    image = models.ImageField(upload_to="products/", verbose_name="Изображение")
    order = models.PositiveIntegerField(default=1, verbose_name="Порядок отображения")

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"
        ordering = ["order"]