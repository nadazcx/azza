from django.db import models
from accounts.models import CustomUser
class Facture(models.Model):
    numero = models.CharField(max_length=100)
    date_emission = models.DateField()
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # ForeignKey to Client
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f'Facture {self.numero} - {self.client.name}'