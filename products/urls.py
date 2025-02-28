from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BannerViewSet, CategoryViewSet, ProductTypeViewSet, BrandViewSet

router = DefaultRouter()
router.register(r'models', BannerViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'categories', CategoryViewSet)  # 👈 Теперь категории работают через ViewSet
router.register(r'product-types', ProductTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
