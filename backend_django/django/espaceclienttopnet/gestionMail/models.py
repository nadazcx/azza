# gestionMail/models.py

from django.db import models

class Email(models.Model):
    addresse = models.CharField(max_length=100)
    emailRecuperation = models.EmailField()
    messages = models.CharField(max_length=100)
    
    status = models.CharField(max_length=20, default='Active')
    adminResulat = models.CharField(max_length=100, default='pending')

    def __str__(self):
        return self.addresse
