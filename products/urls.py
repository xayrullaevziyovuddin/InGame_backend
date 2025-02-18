from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BannerViewSet, CategoryDetailView, CategoryListView, ProductTypeViewSet, BrandViewSet

router = DefaultRouter()
router.register(r'models', BannerViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'product-types', ProductTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("categories/", CategoryListView.as_view(), name="category-list-create"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
]

