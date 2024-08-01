
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("item.urls")),
    path('api/', include(router.urls)),
]