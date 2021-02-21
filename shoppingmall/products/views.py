from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, mixins, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """상품 뷰셋"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('-id')
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name', 'manufacturer']
    ordering_fields = ['id', 'price']
    filterset_fields = ['manufacturer']

    def get_permissions(self):
        """유저 상품 조회를 위한 오버라이딩 함수"""
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]
        
        return super(ProductViewSet, self).get_permissions()
