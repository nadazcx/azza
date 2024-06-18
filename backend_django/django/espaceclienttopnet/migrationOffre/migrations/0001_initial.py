# Generated by Django 5.0.6 on 2024-06-18 02:12

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
            name='MigrationOffre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerooffre', models.IntegerField()),
                ('dateemission', models.DateTimeField(auto_now_add=True)),
                ('ancienne_offre', models.TextField()),
                ('nouvelle_offre', models.TextField()),
                ('statut', models.CharField(choices=[('en_attente', 'En attente'), ('en_cours', 'En cours'), ('acceptee', 'Acceptee'), ('refusee', 'Refusee')], default='en_attente', max_length=10)),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_offres', to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
