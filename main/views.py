from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product

# огранчение на изменения и чтения
from rest_framework.permissions import IsAdminUser

from rest_framework.decorators import action

from rest_framework.response import Response

from .filters import ProductFilter

# для поиска по нескольким полям
from django.db.models import Q

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    # permission_classes = [IsAdminUser] ограничение
    filterset_class = ProductFilter
    # filterset_fields = ['category', 'status']

    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]


    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING),
    ])
    @action(['GET'], detail=False)
    def search(self, request):
        # /products/search/?q=hello
        # query_param = {'q' : 'hello'}
        q = request.query_params.get('q')
        # get_queryset - Products.objects.all()
        queryset = self.get_queryset()
        if q:
            # для поиска только по одному полю
            # queryset = queryset.filter(title__icontains=q) # title ilike '%hello%'
            # для поиска по нескольким полям
            queryset = queryset.filter(Q(title__icontains=q) | Q(descripiton__icontains=q))
            # title ilike '%hello%' or description ilike '%hello%'
        # get_serializer - ProductSerializer
        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=200)