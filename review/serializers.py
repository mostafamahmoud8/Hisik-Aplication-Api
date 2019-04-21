from rest_framework import serializers
from .models import Review
from product.serializer import ProductSerializer

class ReviewSerializer(serializers.ModelSerializer):
    productDetails=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model= Review
        fields=('id','user','text','rate','product','productDetails')
    
    
    def get_productDetails(self,obj):
         return ProductSerializer(obj.product).data
    
    


           
    