from django import forms
from .models import Facture

# Création d'un formulaire pour le modèle Facture
class FactureForm(forms.ModelForm):
    # Création de la classe Meta
    class Meta:
        # Spécifiez le modèle à utiliser
        model = Facture
        
        # Spécifiez les champs à utiliser
        fields = [
            "numero",
            "date_emission",
            "client",
            "montant",
            "description",
        ]
