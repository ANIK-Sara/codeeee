# Generated by Django 5.0.2 on 2024-05-16 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_pharmacommandes_pharmacie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livreur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_liv', models.CharField(max_length=100)),
                ('num_tel', models.CharField(max_length=15)),
                ('adresse_liv', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_livreur',
            field=models.BooleanField(default=False, verbose_name='Is livreur'),
        ),
    ]
