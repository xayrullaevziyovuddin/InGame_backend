# Файл: products/serializers/products.py

from rest_framework import serializers
from ..models import Product, ProductImage, ProductAttribute
from .brands import BrandSerializers
from .categories import CategorySerializer, ProductTypeSerializer
from attributes.serializers import AttributeSerializer


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image", "order"]


class ProductAttributeSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(read_only=True)

    class Meta:
        model = ProductAttribute
        fields = ["id", "attribute"]


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializers(read_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.brand.field.related_model.objects.all(),
        source="brand",
        write_only=True
    )

    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.category.field.related_model.objects.all(),
        source="category",
        write_only=True
    )

    product_type = ProductTypeSerializer(read_only=True)
    product_type_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.product_type.field.related_model.objects.all(),
        source="product_type",
        write_only=True
    )

    images = ProductImageSerializer(many=True, read_only=True)
    attributes_info = serializers.SerializerMethodField()
    discount_percentage = serializers.SerializerMethodField()
    final_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id", "name", "slug", "description", "price", "discount_price",
            "stock", "is_active", "created_at", "updated_at", "main_image",
            "brand", "brand_id", "category", "category_id",
            "product_type", "product_type_id", "images",
            "attributes_info", "discount_percentage", "final_price"
        ]
        extra_kwargs = {
            "slug": {"read_only": True},  # Slug будет генерироваться автоматически
        }

    def get_attributes_info(self, obj):
        product_attributes = ProductAttribute.objects.filter(product=obj)
        return ProductAttributeSerializer(product_attributes, many=True).data

    def get_discount_percentage(self, obj):
        return obj.get_discount_percentage()

    def get_final_price(self, obj):
        return obj.get_final_price()


class ProductListSerializer(serializers.ModelSerializer):
    """Облегченный сериализатор для списка товаров"""
    brand = serializers.StringRelatedField()
    discount_percentage = serializers.SerializerMethodField()
    final_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id", "name", "slug", "price", "discount_price",
            "main_image", "brand", "discount_percentage", "final_price"
        ]

    def get_discount_percentage(self, obj):
        return obj.get_discount_percentage()

    def get_final_price(self, obj):
        return obj.get_final_price()