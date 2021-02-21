from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet


router = DefaultRouter()
router.register('', ProductViewSet)

app_name = 'products'

urlpatterns = [
    path('', include(router.urls))
]
