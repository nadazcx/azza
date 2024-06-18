# transferligne/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransferLignesViewSet

router = DefaultRouter()
router.register(r'transfer-lignes', TransferLignesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
