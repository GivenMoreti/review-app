from django.contrib import admin
from django.urls import path
from . import views
from .views import ItemListCreateAPIView, ItemDetailAPIView

urlpatterns = [
    path("",views.home,name='home'),
    path("add_review",views.create_item,name="create_item")

    ,
    path('api/items/', ItemListCreateAPIView.as_view(), name='item-list-create'),
    path('api/items/<int:pk>/', ItemDetailAPIView.as_view(), name='item-detail'),
]
