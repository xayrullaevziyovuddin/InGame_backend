from django.contrib import admin
from .models import Category, ProductType


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "parent")  # Отображаемые поля
    search_fields = ("name", "slug")  # Поля для поиска
    list_filter = ("parent",)  # Фильтр по родительской категории
    prepopulated_fields = {"slug": ("name",)}  # Автозаполнение slug по name


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")  # Отображаемые поля
    search_fields = ("name",)
    list_filter = ("category",)  # Фильтр по категориям
