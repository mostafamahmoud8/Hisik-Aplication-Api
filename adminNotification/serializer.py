from rest_framework import serializers 
from .models import NotificationAdmin

class NotificationAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model : NotificationAdmin
        fields: ('status','type','ProductReviewID','ScanId',' updated','timestamp')