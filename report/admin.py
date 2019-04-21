from django.contrib import admin
from .models  import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
     list_dispaly=('proudct','user')
     fields=[
             'proudct'
             ,'user'
             ,'Description'
             ,'name'
             ,'brand'
             ,'category'
             ,'comment'
             ,'updated'
             ,'timestamp'
        ]
