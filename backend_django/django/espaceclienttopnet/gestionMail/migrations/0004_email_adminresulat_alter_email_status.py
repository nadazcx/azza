# Generated by Django 5.0.6 on 2024-06-17 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionMail', '0003_rename_address_email_addresse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='adminResulat',
            field=models.CharField(default='pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='email',
            name='status',
            field=models.CharField(default='Active', max_length=20),
        ),
    ]
