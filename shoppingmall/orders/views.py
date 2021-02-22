from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from core.models import User
from products.models import Product
from .models import Order, OrderItem, OrderStatus
from .permissions import IsUserOrAdmin
from .serializers import OrderSerializer, OrderItemSerializer


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """주문 뷰셋"""
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('-id')
    authentication_classs = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsUserOrAdmin]


class OrderItemViewSet(viewsets.ModelViewSet):
   serializer_class = OrderItemSerializer
   queryset = OrderItem.objects.all().order_by('-id')
   authentication_classs = [TokenAuthentication]
   permission_classes = [IsAuthenticated, IsUserOrAdmin]

   def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      self.perform_create(serializer)
      headers = self.get_success_headers(serializer.data)
      return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
