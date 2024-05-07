from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , redirect 
from .forms import SignUpForm , LoginForm
from django.contrib.auth import authenticate , login
from . models import Medecin , Patient , Pharmacie  , Produit 
from django.shortcuts import render, redirect , get_object_or_404
from django.core.exceptions import ValidationError
from .models import  Medecin, Patient, Pharmacie , Produit , Ordonnance , Commande 
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.http import JsonResponse
from .models import Pharmacie
from django.core.paginator import Paginator 
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import logging
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import auth 


logger = logging.getLogger(__name__)

import json
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import  Patient, Medecin, Pharmacie , PharmaCommandes
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm

# Create your views here.
def index(request):
    return render(request , 'app1/index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user = form.save(commit=False)
            user.num_tel = form.cleaned_data['num_tel']
            user.adresse = form.cleaned_data['adresse']
            user.save()
            if user.is_medecin:
                user.save()
                Medecin.objects.create(user=user , nom_medecin=user.username ,
                  
                    num_tel=user.num_tel,
                    adresse=user.adresse,  
                    adresse_cabinet=form.cleaned_data.get('adresse_cabinet', ''),
                    heure_ouverture=form.cleaned_data.get('heure_ouverture', None),
                    heure_fermeture=form.cleaned_data.get('heure_fermeture', None),
                    jours_travail=form.cleaned_data.get('jours_travail', ''),
                    specialite=form.cleaned_data.get('specialite', ''))
            elif user.is_pharmacie:
                user.save()
                Pharmacie.objects.create(user=user ,  num_tel=user.num_tel,
                    adresse=user.adresse, nom_pharmacie=user.username,heure_ouverturep=form.cleaned_data.get('heure_ouverturep', None),
                    heure_fermeture=form.cleaned_data.get('heure_fermeturep', None),
                    nom_responsable=form.cleaned_data.get('nom_responsablep', ''))
            elif user.is_patient:
                user.save()
                Patient.objects.create(user=user , num_tel=user.num_tel,
                    adresse=user.adresse, nom_patient=user.username,
                                        sexe=form.cleaned_data.get('sexe', ''),
                    date_naissance=form.cleaned_data.get('date_naissance', None))
            msg = 'user created'
            return redirect('login_view')
        else:
            print("Form is not valid:", form.errors)
            msg = 'form is not valid '
    else:
        form = SignUpForm()
    return render(request , 'app1/register.html' , {'form': form , 'msg' : msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            if user is not None and user.is_admin:
                login(request , user) 
                return redirect ('admin')
            elif  user is not None and user.is_medecin:
                login(request , user) 
                return redirect ('medecin')
            elif user is not None and user.is_pharmacie:
                login(request , user) 
                return redirect ('pharmacie')
            elif user is not None and user.is_patient:
                login(request , user) 
                return redirect ('patient')
            else:
                msg = 'invalid credentials'
        else: 
            msg = 'error validation form'
    return render (request , 'app1/login.html' , {'form': form  , 'msg' : msg})


def admin(request):
    return render(request , 'app1/admin.html')

def medecin(request):
    return render(request , 'app1/medecin.html')
def pharmacie(request):
    return render(request , 'app1/pharmacie.html')
def patient(request):
     query = request.GET.get('query', '')

    # Initialisation des résultats
     medecins = Medecin.objects.none()
     pharmacies = Pharmacie.objects.none()
     produits = Produit.objects.none()
     pharmacies_avec_produits = Pharmacie.objects.none() 

    # Rechercher des médecins par nom ou spécialité
     if query:
        medecins = Medecin.objects.filter(nom_medecin__icontains=query )| \
               Medecin.objects.filter(specialite__icontains=query) | \
               Medecin.objects.filter(adresse_cabinet__icontains=query) 
        
        

        # Rechercher des pharmacies par nom ou nom du responsable
        pharmacies = Pharmacie.objects.filter(nom__icontains=query)| \
                 Pharmacie.objects.filter(adresse__icontains=query)
        
        # Rechercher des produits par nom
        produits = Produit.objects.filter(nom_pr__icontains=query)
         # Récupérer les pharmacies associées aux produits trouvés
        if produits.exists():
            pharmacies_avec_produits = Pharmacie.objects.filter(produits__in=produits)

    # Pagination
     paginator = Paginator(medecins, 8)  # 8 résultats par page
     page_number = request.GET.get('page')
     medecin_page = paginator.get_page(page_number) 

     paginator = Paginator(pharmacies, 8)  # 8 résultats par page
     page_number = request.GET.get('page')
     pharmacie_page = paginator.get_page(page_number)

     paginator = Paginator(produits, 8)  # 8 résultats par page
     page_number = request.GET.get('page')
     produit_page = paginator.get_page(page_number)

     paginator = Paginator(pharmacies_avec_produits, 8)
     pharmacies_avec_produits_page = paginator.get_page(request.GET.get('page'))

    # Rendu de la vue avec les résultats paginés
     return render(request, 
        'app1/patient.html', 
        {
            'medecins': medecin_page,
            'pharmacies': pharmacie_page,
            'produits': produit_page,
            'pharmacies_avec_produits': pharmacies_avec_produits_page,

            'query': query,  # Conserver la valeur de recherche pour affichage
        })
     

   

def pharmacie_details(request, pharmacie_id):
    pharmacie = get_object_or_404(Pharmacie, pk=pharmacie_id)
    product_objectt = pharmacie.produits.all()  # Utilisation de la relation avec le modèle de produit
    
    item_namee = request.GET.get('item-namee')
    print("Valeur de item_namee:", item_namee)  # Afficher la valeur de item_namee
    
    if item_namee and item_namee.strip():  # Vérifie si item_namee n'est pas vide
        product_objectt = product_objectt.filter(nom_pr__icontains=item_namee)
    
    print("Produits filtrés:", product_objectt)  # Afficher les produits filtrés
    
    return render(request, 'app3/pharmacie_details.html', {'pharmacie': pharmacie, 'product_objectt': product_objectt,})


def footer(request):
    return render(request , 'app1/footer.html')

def confirmationpharm (request):
    info = PharmaCommandes.objects.all()[:1]
    for item in info:
        nom = item.nom_utilisateur 
    
    return render (request , 'app1/confirmationphar.html' , {'nameph' : nom })






def pharmacie_details(request, pharmacie_id):
    pharmacie = get_object_or_404(Pharmacie, pk=pharmacie_id)
    product_objectt = pharmacie.produits.all()  # Utilisation de la relation avec le modèle de produit
    
    item_namee = request.GET.get('item-namee')
    print("Valeur de item_namee:", item_namee)  # Afficher la valeur de item_namee
    
    if item_namee and item_namee.strip():  # Vérifie si item_namee n'est pas vide
        product_objectt = product_objectt.filter(nom_pr__icontains=item_namee)
    
    print("Produits filtrés:", product_objectt)  # Afficher les produits filtrés
    
    return render(request, 'app3/pharmacie_details.html', {'pharmacie': pharmacie, 'product_objectt': product_objectt,})
def checkoutout(request):
    ordonnance_requise = False  # Par défaut, on considère que l'ordonnance n'est pas requise
    panier = {}  # Initialisez le panier pour éviter les erreurs UnboundLocalError

    if request.method == "POST":
        # Récupérer le panier depuis le champ caché
        panier_str = request.POST.get('items', '{}')  # Assurez-vous que vous récupérez la clé correcte
        panier = json.loads(panier_str)  # Convertir en objet Python

        # Déterminer si une ordonnance est requise
        for produit in panier.values():
            if len(produit) > 3 and produit[3]:  # Si le produit nécessite une ordonnance
                ordonnance_requise = True
                break  # Sortir de la boucle, une ordonnance suffit

        # Validation du formulaire
        if ordonnance_requise and 'ordonnance' not in request.FILES:
            return render(
                request,
                'app3/checkoutout.html',
                {
                    'panier': panier,
                    'ordonnance_requise': ordonnance_requise,
                    'message_erreur': "Une ordonnance est requise mais n'a pas été fournie."
                }
            )

        # Récupérer les champs du formulaire
        nom_utilisateur = request.POST.get('nom')
        prenom_utilisateur = request.POST.get('prenom')
        adr_mail = request.POST.get('email')
        num_tel = request.POST.get('tel')
        adresse = request.POST.get('address')
        ville = request.POST.get('ville')
        total = request.POST.get('total', '0')  # Valeur par défaut si manquant
        items = request.POST.get('items')

        # Sauvegarder la commande
        pharcom = PharmaCommandes(
            nom_utilisateur=nom_utilisateur,
            prenom_utilisateur=prenom_utilisateur,
            total=total,
            adr_mail=adr_mail,
            num_tel=num_tel,
            adresse=adresse,
            ville=ville,
            items=items,
            ordonnance=request.FILES.get('ordonnance', None)  # Récupérer l'ordonnance si fournie
        )
        pharcom.save()

        # Rediriger vers la confirmation
        return redirect('confirmationpharm')

    # Pour une requête GET, renvoyer le formulaire
    return render(
        request,
        'app3/checkoutout.html',
        {
            'panier': panier,  # Inclure le panier
            'ordonnance_requise': ordonnance_requise  # Indicateur pour le front-end
        }
    )



def medecin_details(request, medecin_id):
        medecin = get_object_or_404(Medecin, id_medecin=medecin_id)
        return render(request, 'app3/medecin_details.html', {'medecin': medecin})


