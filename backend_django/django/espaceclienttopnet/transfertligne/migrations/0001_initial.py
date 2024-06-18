# Generated by Django 5.0.6 on 2024-06-15 20:32

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
            name='TransferLignes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_ligne', models.IntegerField(unique=True)),
                ('date_transfer', models.DateTimeField(auto_now_add=True)),
                ('ancienne_addresse', models.CharField(max_length=255)),
                ('nouvelle_addresse', models.CharField(max_length=255)),
                ('statut', models.CharField(choices=[('en_attente', 'En attente'), ('accepte', 'Accepté'), ('refuse', 'Refusé')], default='en_attente', max_length=10)),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_transfers', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]