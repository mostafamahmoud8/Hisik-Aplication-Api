from django.shortcuts import render
from .models import NotificationUser
from rest_framework import generics
from .serializer import UserNotificationSerializer
class UserNotificationListView(generics.ListCreateAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = NotificationUser.objects.all()
    serializer_class            = UserNotificationSerializer


class UserNotificationDetailedView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = NotificationUser.objects.all()
    serializer_class            = UserNotificationSerializer
    lookup_field                = 'type'
