# Generated by Django 5.0.6 on 2024-06-16 21:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reclamation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('statut', models.CharField(choices=[('en_attente', 'En attente'), ('en_cours', 'En cours'), ('resolue', 'Résolue')], default='en_attente', max_length=10)),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_reclamations', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
