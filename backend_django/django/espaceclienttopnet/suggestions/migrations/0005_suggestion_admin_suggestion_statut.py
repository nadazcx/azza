# Generated by Django 5.0.6 on 2024-06-18 00:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0004_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_suggestions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='statut',
            field=models.CharField(choices=[('en_attente', 'En attente'), ('en_cours', 'En cours'), ('acceptee', 'acceptee')], default='en_attente', max_length=10),
        ),
    ]
