from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is_admin' , default=False)
    is_medecin= models.BooleanField('Is medecin' , default=False)
    is_pharmacie= models.BooleanField('Is pharmacie' , default=False)
    is_patient= models.BooleanField('Is patient' , default=False)

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom_Admin = models.CharField(max_length=255 , default="Admin")
    password = models.CharField(max_length=255, blank=True, null=True)

class Medecin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom_medecin = models.CharField(max_length=255 , default="Medecin Anonyme")
    adresse_cabinet = models.CharField(max_length=255, blank=True, null=True)
    heure_ouverture = models.TimeField(blank=True, null=True)
    heure_fermeture = models.TimeField(blank=True, null=True)
    jours_travail = models.CharField(max_length=255, blank=True, null=True)
    specialite = models.CharField(max_length=255, blank=True, null=True)
    num_tel = models.CharField(max_length=15, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)

class Produit(models.Model):
    id_produit = models.AutoField(primary_key=True)
    nom_pr = models.CharField(max_length=100)
    Description = models.CharField(max_length=10000 , null=True)

    prix_unitaire = models.DecimalField(
        max_digits=10, decimal_places=2, default=None)
    
    image = models.CharField( max_length=2000   , default=None, null=True)

    TYPE_CHOICES = [
        ('Pharmaceutique', 'Produit Pharmaceutique'),
        ('Medicament', 'Médicament'),
    ]
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    Qte = models.CharField(max_length=100, blank=True, null=True)

    # Attributs spécifiques aux produits pharmaceutiques
    dosage = models.CharField(max_length=100, blank=True, null=True)
    ordonnance_requise = models.BooleanField(default=False)



    def __str__(self):
        return self.nom_pr

class Pharmacie(models.Model):
    

    user = models.OneToOneField(User, on_delete=models.CASCADE , primary_key=True)

    nom = models.CharField(max_length=255)
    heure_ouverturep = models.TimeField(blank=True, null=True)
    heure_fermeturep = models.TimeField(blank=True, null=True)
    nom_responsable = models.CharField(max_length=255, blank=True, null=True)
    num_tel = models.CharField(max_length=15, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    produits = models.ManyToManyField(Produit)
    def __str__(self):
        return self.nom
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom_patient = models.CharField(max_length=255)
    sexe = models.CharField(max_length=1, blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    num_tel = models.CharField(max_length=15, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)


class Commande(models.Model):
    id_commande = models.AutoField(primary_key=True)
    nom_utilisateur = models.CharField(max_length=100 , default=None)
    total = models.CharField(max_length=200 , default=None)
    date_commande = models.DateTimeField(auto_now=True)
    ville = models.CharField(max_length=100 )
    adr_mail = models.CharField(max_length=100 , default=None)
    adresse =  models.CharField(max_length=100 , default=None)
    num_tel = models.CharField(max_length=15, null=True)
    pharmacie = models.ForeignKey(Pharmacie, on_delete=models.CASCADE, related_name="commandes")

    items = models.CharField(max_length=300 , default=None)
   
    class Meta:
        ordering = ['-date_commande']
    def __str__(self):
        return self.nom_utilisateur 

   
class Produit_Prescris(Produit):
    id_produitprescris = models.AutoField(primary_key=True)
    nom_prp = models.CharField(max_length=100)
    Descriptionp= models.CharField(max_length=10000 , null=True)

class Ordonnance(models.Model):
    id_ordonnance = models.AutoField(primary_key=True, default=None)
    
    nom_medecin = models.CharField(max_length=100, default=None)
   
    adresse_cabinet = models.CharField(max_length=255, default=None)
    specialite = models.CharField(max_length=100, default=None)

    nom_patient = models.CharField(max_length=100, default=None)
    prenom_patient = models.CharField(max_length=10, default=None)
    num_tel = models.CharField(max_length=20 , default = None)
    
    liste_produits = models.CharField(max_length=1000 , default = None)

class PharmaCommandes(models.Model):
    id_commandepharm = models.AutoField(primary_key=True)
    nom_utilisateur = models.CharField(max_length=100 , default=None)
    prenom_utilisateur = models.CharField(max_length=100 , default=None)
    total = models.CharField(max_length=200 , default=None)
    date_commande = models.DateTimeField(auto_now=True)
    ville = models.CharField(max_length=100 )
    adr_mail = models.CharField(max_length=100 , default=None)
    adresse =  models.CharField(max_length=100 , default=None)
    num_tel = models.CharField(max_length=15, null=True)

    items = models.CharField(max_length=300 , default=None)
    ordonnance = models.FileField(upload_to='ordonnances/', null=True, blank=True)  # Le paramètre 'upload_to' spécifie où stocker les fichiers

    class Meta:
        ordering = ['-date_commande']
    def __str__(self):
        return self.nom_utilisateur 
