from rest_framework import serializers 
from report.models import Report 

class ReportSerializers(serializers.ModelSerializer):
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

