from rest_framework import serializers
from .models import MigrationOffre

class MigrationOffreSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()

    class Meta:
        model = MigrationOffre
        fields = ['id', 'client', 'client_name', 'numerooffre', 'dateemission', 'ancienne_offre', 'nouvelle_offre', 'statut', 'admin']
        read_only_fields = ['client', 'admin', 'dateemission']

    def get_client_name(self, obj):
        return obj.client.name if obj.client.name else obj.client.email

    def validate(self, data):
        request = self.context.get('request')
        client = request.user
        numerooffre = data.get('numerooffre')

        # Check if there is any pending offer with the same numerooffre
        if MigrationOffre.objects.filter(client=client, numerooffre=numerooffre, statut='en_attente').exists():
            raise serializers.ValidationError(f'You already have a pending offer for number {numerooffre}.')

        return data

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['client'] = request.user
        return super().create(validated_data)
