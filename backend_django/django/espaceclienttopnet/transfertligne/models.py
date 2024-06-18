# transferligne/models.py

from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class TransferLignes(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('accepte', 'Accepté'),
        ('refuse', 'Refusé')
    ]

    numero_de_ligne = models.IntegerField()
    date_transfer = models.DateTimeField(auto_now_add=True)
    ancienne_addresse = models.CharField(max_length=255)
    nouvelle_addresse = models.CharField(max_length=255)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='en_attente')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='admin_transfers', null=True, blank=True)


    def __str__(self):
            return self.sujet

    def accepter_demande(self, admin_user):
        self.statut = 'accepte'
        self.admin = admin_user
        self.save()

    def refuser_demande(self, admin_user):
        self.statut = 'refuse'
        self.admin = admin_user
        self.save()
