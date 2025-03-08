from .banners import BannerSerializer
from .categories import CategorySerializer, ProductTypeSerializer
from .brands import BrandSerializers
from .products import ProductSerializer, ProductListSerializer  # добавляем оба сериализатора

__all__ = [
    "BannerSerializer",
    "CategorySerializer",
    "ProductTypeSerializer",
    "BrandSerializers",
    "ProductSerializer",
    "ProductListSerializer"
]
