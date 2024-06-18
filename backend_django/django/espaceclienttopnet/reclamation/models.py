# reclamations/models.py

from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Reclamation(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('acceptee', 'acceptee')
    ]

    numero = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='en_attente')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='admin_reclamations', null=True, blank=True)

    def __str__(self):
        return f'Reclamation {self.numero} - {self.user.username}'

    def accepter_reclamation(self, admin_user):
        self.statut = 'acceptee'
        self.admin = admin_user
        self.save()

    def resoudre_reclamation(self, admin_user):
        self.statut = 'resolue'
        self.admin = admin_user
        self.save()

    def refuser_reclamation(self, admin_user):
        self.statut = 'refuse'
        self.admin = admin_user
        self.save()
