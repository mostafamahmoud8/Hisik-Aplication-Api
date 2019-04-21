from rest_framework import serializers
from .models import Replay,Review
from review.serializers import ReviewSerializer

class ReplaySerializer(serializers.ModelSerializer):
    AllReviews=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model= Replay
        fields=('id','review','user','text','AllReviews')
    
    def get_AllReviews(self,obj):
         return ReviewSerializer(obj.review).data

           
    