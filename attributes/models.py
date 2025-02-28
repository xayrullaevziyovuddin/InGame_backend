from django.db import models


class AttributeType(models.Model):
    """Тип характеристики (например, 'Тип', 'Конструкция', 'Частота')"""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    """Значение характеристики (например, 'Проводные наушники')"""
    attbute_type = models.ForeignKey(AttributeType, on_delete=models.CASCADE, related_name="attributes")
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.attbute_type.name}: {self.value}"


