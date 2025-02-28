from rest_framework import serializers
from ..models import Category, ProductType


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "parent", "subcategories"]  # 👈 Исправлено!

    def get_subcategories(self, obj):
        subcategories = obj.subcategories.all()
        return CategorySerializer(subcategories, many=True).data


class ProductTypeSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # В ответе будет объект категории
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )  # Позволяет передавать ID категории при создании

    class Meta:
        model = ProductType
        fields = ["id", "name", "category", "category_id"]



