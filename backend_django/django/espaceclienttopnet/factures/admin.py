from django.contrib import admin
from .models import Facture
# Register your models here.

@admin.register(Facture)
class FacturesAdmin(admin.ModelAdmin):
    list_display = ('numero', 'date_emission', 'client', 'montant')
    search_fields = ('numero', 'client')
    list_filter = ('date_emission',)

