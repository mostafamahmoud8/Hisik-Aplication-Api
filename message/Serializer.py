from rest_framework import serializers 
from .models import Message
from User.serializers import UserSerializers
from product.serializer import ProductSerializer

class MessageSerializers(serializers.ModelSerializer):
    PopUser=serializers.SerializerMethodField(read_only=True)
    PopProduct=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model  = Message
        fields = [
            'text',
            'user',
            'updated',
            'timestamp'
        ]

    def get_PopUser(self,obj):
         return User(obj.user).data

    def get_PopProduct(self,obj):
         return ProductSerializer(obj.product).data