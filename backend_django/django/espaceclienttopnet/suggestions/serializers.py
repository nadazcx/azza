from rest_framework import serializers
from .models import Suggestion
from accounts.models import CustomUser  # Adjust the import path as per your project structure

class SuggestionSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Suggestion
        fields = ['id', 'sujet', 'description', 'user_name', 'statut']

    def get_user_name(self, obj):
        return obj.user.name if obj.user.name else obj.user.email
