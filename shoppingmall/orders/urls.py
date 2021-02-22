from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet, OrderItemViewSet


router = DefaultRouter()
router.register('', OrderViewSet)
router.register('items', OrderItemViewSet)

app_name = 'orders'

urlpatterns = [
    path('', include(router.urls))
]
