from django.shortcuts import render
from .models import Search 
from product.models import Product
from brand.models import Brand
from category.models import Category
from product.serializer import ProductSerializer
from .Serializers import SearchSerializers
from rest_framework import generics
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.decorators import api_view

# import pandas as pd
# import numpy as ny


class SearchListView(generics.ListCreateAPIView):
    permission_classes       = []
    authentication_classes   = []
    queryset                 = Search.object.all()
    serializer_class         = SearchSerializers

class SearchDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes       = []
    authentication_classes   = []
    queryset                 = Search.object.all()
    serializer_class         = SearchSerializers
    lookup_field             = 'id'

@api_view(['GET'])
def PopualerSearch(request):
    final=[]
    ser = {}
    res= Search.object.values('id','text','user','product').annotate(dcount=Count('product__id')).order_by('-dcount')[:5]
    pro= Product.objects.get(id=res[0]['product'])
    for i in res :
       pro= Product.objects.get(id=i['product'])
       ser = ProductSerializer(pro).data
       final.append(ser)
    return Response(final)

@api_view(['GET'])
def RecommandedSearch(request):
    res  = Search.object.values('id','text','user','product')
    res2 = Brand.objects.values('id','Name')
    res3 = Category.objects.values('id','Name')
    df   = pd.merge(res,res2,res3,on='id')
    #queryset = Search.object.all().select_related('user').select_related('product')
    return Response('df')


