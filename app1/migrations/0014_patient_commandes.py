# Generated by Django 5.0.2 on 2024-05-17 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_pharmacommandes_livreur'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='commandes',
            field=models.ManyToManyField(to='app1.pharmacommandes'),
        ),
    ]
