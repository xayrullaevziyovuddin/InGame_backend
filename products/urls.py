from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BannerViewSet, CategoryViewSet, ProductTypeViewSet, BrandViewSet, ProductViewSet  # Add ProductViewSet here

router = DefaultRouter()
router.register(r'models', BannerViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'product-types', ProductTypeViewSet)
router.register(r'products', ProductViewSet)  # Add this line to register the ProductViewSet

urlpatterns = [
    path('', include(router.urls)),
]