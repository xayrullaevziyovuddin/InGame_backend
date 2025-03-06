from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttributeTypeViewSet, AttributeViewSet

router = DefaultRouter()
router.register(r'attribute-types', AttributeTypeViewSet)
router.register(r'attributes', AttributeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
