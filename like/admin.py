from django.contrib import admin
from .models import Like

@admin.register(Like)

class replay_admin(admin.ModelAdmin):
    list_display=('like','review','user')
    fields=[
            'like',
            'review',
            'user',
             
        ]
    