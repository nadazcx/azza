from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MigrationOffreViewSet

router = DefaultRouter()
router.register(r'migration-offres', MigrationOffreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
