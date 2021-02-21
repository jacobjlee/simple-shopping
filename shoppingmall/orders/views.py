from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from core.models import User
from products.models import Product
from .models import Order, OrderItem, OrderStatus
from .permissions import IsUserOrAdmin
from .serializers import OrderSerializer


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """주문 뷰셋"""
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    authentication_classs = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsUserOrAdmin]
