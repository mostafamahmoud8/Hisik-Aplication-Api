from django.shortcuts import render
from .models import Product
from .serializer import ProductSerializer
from .filter import ProductFilter
from rest_framework import generics
# Create your views here. 
class ProductListView(generics.ListCreateAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               =  Product.objects.all()
    serializer_class       =  ProductSerializer
    filterset_class        =  ProductFilter
    search_fields          = ('id','Category__Name','brand__Name','name',)

    # def get_queryset(self):
    #     category = self.request.GET.get('Cname')
    #     qs = Product.objects.filter(Category__Name=category)
    #     return qs
     


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               =  Product.objects.all()
    serializer_class       =  ProductSerializer
    lookup_field = 'id'
    