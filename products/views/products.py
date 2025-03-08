from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
import django_filters

from ..models import Product
from ..serializers import ProductSerializer, ProductListSerializer

class ProductFilter(FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    brand = django_filters.CharFilter(field_name="brand__name", lookup_expr="iexact")
    brands = django_filters.CharFilter(method="filter_brands")
    category = django_filters.CharFilter(field_name="category__slug", lookup_expr="exact")
    product_type = django_filters.CharFilter(field_name="product_type__name", lookup_expr="iexact")
    is_discount = django_filters.BooleanFilter(method="filter_discount")
    in_stock = django_filters.BooleanFilter(field_name="stock", method="filter_stock")
    attribute = django_filters.CharFilter(method="filter_attribute")

    def filter_brands(self, queryset, name, value):
        brand_ids = [int(x) for x in value.split(",") if x.isdigit()]
        return queryset.filter(brand__id__in=brand_ids)

    def filter_discount(self, queryset, name, value):
        if value:
            return queryset.filter(discount_price__isnull=False)
        return queryset

    def filter_stock(self, queryset, name, value):
        if value:
            return queryset.filter(stock__gt=0)
        return queryset

    def filter_attribute(self, queryset, name, value):
        try:
            attr_type_id, value_id = value.split(":")
            return queryset.filter(attributes__attribute_type_id=attr_type_id, attributes__id=value_id)
        except ValueError:
            return queryset

    class Meta:
        model = Product
        fields = ["brand", "category", "product_type", "is_discount", "in_stock"]

class ProductViewSet(viewsets.ModelViewSet):
    """API для работы с товарами"""
    queryset = Product.objects.filter(is_active=True)
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "description"]
    ordering_fields = ["price", "created_at", "name"]
    ordering = ["-created_at"]

    def get_serializer_class(self):
        """Возвращает разные сериализаторы для списка и детальной информации"""
        if self.action == "list":
            return ProductListSerializer
        return ProductSerializer

    @action(detail=False, methods=["get"])
    def featured(self, request):
        """Получение рекомендуемых товаров"""
        featured_products = self.get_queryset().filter(is_active=True)[:10]
        serializer = ProductListSerializer(featured_products, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def discounts(self, request):
        """Получение товаров со скидками"""
        discounted = self.get_queryset().filter(discount_price__isnull=False)
        serializer = ProductListSerializer(discounted, many=True)
        return Response(serializer.data)
