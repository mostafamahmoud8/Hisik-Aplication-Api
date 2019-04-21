from django.contrib import admin
from .models import NotificationUser
@admin.register(NotificationUser)
class Admin_NotificationUser(admin.ModelAdmin):
    list_display = ('Status','Type','user','product','review','updated','timestamp')
    fields = ('Status','Type','user','product','review')

