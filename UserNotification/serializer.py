from .models import NotificationUser
from rest_framework import serializers
from product.serializer import ProductSerializer

class UserNotificationSerializer(serializers.ModelSerializer):
    # Notification_user  = serializers.SerializerMethodField(read_only=True)
    Notification_product  = serializers.SerializerMethodField(read_only=True)
    Notification_review  = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model : NotificationUser
        fields :('status'
                ,'type',
                'user',
                'product',
                'review',
                'updated'
                ,'timestamp')


    # def get_Notification_user(self,obj)
    # {
    #     return
    # }    
   
