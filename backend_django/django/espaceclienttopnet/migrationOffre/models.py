from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class MigrationOffre(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('acceptee', 'Acceptee'),
        ('refusee', 'Refusee')
    ]

    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    numerooffre = models.IntegerField()
    dateemission = models.DateTimeField(auto_now_add=True)
    ancienne_offre = models.TextField()
    nouvelle_offre = models.TextField()
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='en_attente')
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='admin_offres', null=True, blank=True)

    def __str__(self):
        return f'Offre {self.numerooffre} - {self.client.username}'

    def accepter_offre(self, admin_user):
        self.statut = 'acceptee'
        self.admin = admin_user
        self.save()

    def refuser_offre(self, admin_user):
        self.statut = 'refusee'
        self.admin = admin_user
        self.save()
