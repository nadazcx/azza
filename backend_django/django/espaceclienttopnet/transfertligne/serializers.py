# transferligne/serializers.py

from rest_framework import serializers
from .models import TransferLignes
from accounts.models import CustomUser  # Adjust the import path as per your project structure

class TransferLignesSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = TransferLignes
        fields = ['id', 'numero_de_ligne', 'date_transfer', 'ancienne_addresse', 'nouvelle_addresse', 'statut', 'user_name', 'admin']

    def get_user_name(self, obj):
        return obj.user.name if obj.user.name else obj.user.email

