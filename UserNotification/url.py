from django.urls import path
from .views import UserNotificationDetailedView, UserNotificationListView

urlpatterns = [
    path('', UserNotificationListView.as_view()),
    path('<str:type>/', UserNotificationDetailedView.as_view()),
]
