# Generated by Django 5.0.6 on 2024-06-05 10:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Facture",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("numero", models.CharField(max_length=100, unique=True)),
                ("date_emission", models.DateField()),
                ("client", models.CharField(max_length=255)),
                ("montant", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
    ]