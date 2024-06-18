# transferligne/admin.py

from django.contrib import admin
from .models import TransferLignes

class TransferLignesAdmin(admin.ModelAdmin):
    list_display = ('numero_de_ligne', 'date_transfer', 'ancienne_addresse', 'nouvelle_addresse', 'statut', 'user', 'admin')
    list_filter = ('statut', 'user', 'admin')
    search_fields = ('numero_de_ligne', 'ancienne_addresse', 'nouvelle_addresse')
    readonly_fields = ('date_transfer',)

admin.site.register(TransferLignes, TransferLignesAdmin)
