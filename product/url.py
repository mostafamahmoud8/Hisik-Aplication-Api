from .views import ProductDetailView,ProductListView
from django.urls import path

urlpatterns = [
    path('', ProductListView.as_view(),name='productListCreate'),
    path('<int:id>/', ProductDetailView.as_view(),name='productDetail'),
]
 
