# Файл: comments/models.py
from django.db import models
from products.models import Product


class Comment(models.Model):
    """Комментарии к товарам от пользователей"""
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comments", verbose_name="Товар"
    )
    author_name = models.CharField(max_length=100, verbose_name="Имя автора")
    author_email = models.EmailField(verbose_name="Email автора")
    text = models.TextField(verbose_name="Текст комментария")
    rating = models.PositiveSmallIntegerField(
        default=5,
        choices=[(i, str(i)) for i in range(1, 6)],
        verbose_name="Оценка"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_approved = models.BooleanField(default=False, verbose_name="Одобрен")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Комментарий от {self.author_name} к {self.product.name}"