from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("add_review",views.create_item,name="create_item")
]
