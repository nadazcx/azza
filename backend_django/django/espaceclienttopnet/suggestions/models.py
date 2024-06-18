from django.db import models
from accounts.models import CustomUser

class Suggestion(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('acceptee', 'acceptee')
    ]

    sujet = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='en_attente')
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='admin_suggestions', null=True, blank=True)

    def __str__(self):
        return self.sujet

    def accepter_suggestion(self, admin_user):
        self.statut = 'acceptee'
        self.admin = admin_user
        self.save()

    def refuser_suggestion(self, admin_user):
        self.statut = 'refusee'
        self.admin = admin_user
        self.save()
