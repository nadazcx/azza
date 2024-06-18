# urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from suggestions.views import SuggestionViewSet
from transfertligne.views import TransferLignesViewSet  # Import TransferLignesViewSet

router = DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reclamation/', include('reclamation.urls')),
    path('factures/', include('factures.urls')),
    path('suggestion/', include('suggestions.urls')),  # Include the URLs from the suggestions app
    path('transfer/', include('transfertligne.urls')),  # Include TransferLignes URLs
    path('api/',include('accounts.urls')),
    path('gestionmail/',include('gestionMail.urls')),
    path('migration_offre/', include('migrationOffre.urls')),  # Include MigrationOffre URLs

    
]