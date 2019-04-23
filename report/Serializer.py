from rest_framework import serializers 
from report.models import Report 
from User.serializers import UserSerializers
from product.serializer import ProductSerializer

class ReportSerializers(serializers.ModelSerializer):
    PopUser=serializers.SerializerMethodField(read_only=True)
    PopProduct=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model  = Report
        fields = [
            'proudct',
            'user',
            'Description',
            'name',
            'brand',
            'category',
            'comment',
            'updated',
            'timestamp'
        ]

    def get_PopUser(self,obj):
         return User(obj.user).data

    def get_PopProduct(self,obj):
         return ProductSerializer(obj.product).data

