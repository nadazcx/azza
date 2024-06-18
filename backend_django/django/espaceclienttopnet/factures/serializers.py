from rest_framework import serializers
from .models import Facture

class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = ('numero', 'date_emission', 'client', 'montant', 'description')