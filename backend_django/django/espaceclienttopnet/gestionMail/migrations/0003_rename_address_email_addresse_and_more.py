# Generated by Django 5.0.6 on 2024-06-17 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionMail', '0002_alter_email_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='address',
            new_name='addresse',
        ),
        migrations.RenameField(
            model_name='email',
            old_name='recovery_email',
            new_name='emailRecuperation',
        ),
        migrations.RenameField(
            model_name='email',
            old_name='quota_used',
            new_name='messages',
        ),
    ]
