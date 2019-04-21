from rest_framework import serializers 
from .models import Message

class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Message
        fields = [
            'text',
            'user',
            'updated',
            'timestamp'
        ]