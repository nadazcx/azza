# reclamations/serializers.py

from rest_framework import serializers
from .models import Reclamation

class ReclamationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamation
        fields = '__all__'
        read_only_fields = ['user', 'admin', 'date']

    def validate(self, data):
        request = self.context.get('request')
        user = request.user
        numero = data.get('numero')
        
        # Check if there is any pending reclamation with the same numero
        if Reclamation.objects.filter(user=user, numero=numero, statut='en_attente').exists():
            raise serializers.ValidationError(f'You already have a pending reclamation for number {numero}.')
        
        return data

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)
