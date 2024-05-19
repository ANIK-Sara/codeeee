from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from .models import User , Produit , Pharmacie  , Livreur , Patient , Medecin , Admin 
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class" : "form-control" 
            }
        )
    )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class" : "form-control" 
            }
        )
    )



class SignUpForm(UserCreationForm):
    # Champs communs à tous les rôles
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    num_tel = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
        label="Numéro de téléphone"
    )
    adresse = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        required=True,
        label="Adresse"
    )
    
    # Champs pour les rôles
    is_medecin = forms.BooleanField(required=False, label="Médecin")
    is_pharmacie = forms.BooleanField(required=False, label="Pharmacie")
    is_patient = forms.BooleanField(required=False, label="Patient")
    is_livreur = forms.BooleanField(required=False, label="Livreur")



    # Champs spécifiques aux rôles
    sexe = forms.ChoiceField(
        choices=[('M', 'Masculin'), ('F', 'Féminin')],
        required=False,
        label="Sexe"
    )
    date_naissance = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Date de naissance"
    )
    adresse_cabinet = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 3}),
        label="Adresse du cabinet"
    )
    heure_ouverture = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={"type": "time"}),
        label="Heure d'ouverture"
    )
    heure_fermeture = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={"type": "time"}),
        label="Heure de fermeture"
    )
    jours_travail = forms.CharField(
        required=False,
        widget=forms.TextInput(),
        label="Jours de travail"
    )
    specialite = forms.CharField(
        required=False,
        widget=forms.TextInput(),
        label="Spécialité"
    )
    nom_responsable = forms.CharField(
        required=False,
        widget=forms.TextInput(),
        label="Nom du responsable"
    )
    heure_ouverturep = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={"type": "time"}),
        label="Heure d'ouverturep"
    )
    heure_fermeturep = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={"type": "time"}),
        label="Heure de fermeturep" )
    # Champ 'disponible'
    disponible = forms.BooleanField(
        required=False,
        label="Disponible"
    )
 # Champ 'ville'
    ville = forms.CharField(
        widget=forms.Select(choices=[
            ('Alger', 'Alger'),
            ('Constantine', 'Constantine'),
            ('Oran', 'Oran'),
            ('Annaba', 'Annaba'),
        ]),
        required=False,
        label="Ville"
    )
    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2', 'num_tel', 'adresse',
            'is_medecin', 'is_pharmacie', 'is_patient', 'is_livreur',
            'sexe', 'date_naissance', 'adresse_cabinet', 'heure_ouverture', 'heure_fermeture',
            'jours_travail', 'specialite', 'nom_responsable' , 'heure_ouverturep', 'heure_fermeturep',
             'disponible' , 'ville' ,
        )

class CustomPharmacieChangeForm(UserChangeForm):
    class Meta:
        model = Pharmacie
        fields = ['nom', 'heure_ouverturep', 'heure_fermeturep', 'nom_responsable', 'num_tel', 'adresse', 'produits']

class CustomLivreurChangeForm(UserChangeForm):
    class Meta:
        model = Livreur
        fields = ['nom_liv', 'num_tel', 'adresse_liv', 'disponible', 'ville']


class CustomPatientChangeForm(UserChangeForm):
    class Meta:
        model = Patient
        fields = ['nom_patient', 'sexe', 'date_naissance', 'num_tel', 'adresse' ]
class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom_pr', 'Description', 'prix_unitaire', 'image', 'type', 'dosage', 'ordonnance_requise', 'Qte']