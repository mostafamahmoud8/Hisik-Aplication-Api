from django.shortcuts import render

from rest_framework import generics

from .models import Like
from .serializer import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               = Like.objects.all()
    serializer_class       = LikeSerializer
    search_field           =('user__UserName','user__id','review__id','review__product','like__id')




class LikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               =  Like.objects.all()
    serializer_class       =  LikeSerializer
    lookup_field= 'id'
    

