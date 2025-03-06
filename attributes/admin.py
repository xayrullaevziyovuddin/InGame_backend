from django.contrib import admin
from .models import Attribute, AttributeType


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ("id", "attribute_type", "value")  # Показывать ID, тип и значение
    list_filter = ("attribute_type",)  # Фильтр по типу характеристики
    search_fields = ("value",)  # Поиск по значению


@admin.register(AttributeType)
class AttributeTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")  # Показывать ID и название в списке
    search_fields = ("name",)  # Поиск по названию
