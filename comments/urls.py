from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'comments', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    # path('something/', views.SomeView.as_view()),  # УДАЛИТЬ!
    # path('something/', views.some_view),  # УДАЛИТЬ!
]