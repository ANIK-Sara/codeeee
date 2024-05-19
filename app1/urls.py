from django.urls import path 
from . import views
from .views import ProductDeleteView

urlpatterns = [
path('' , views.index , name='index'),
path('login/' , views.login_view , name='login_view'),
path('register/' , views.register , name='register'),
path('commande_details/<int:commande_id>/', views.commande_details, name='commande_details'),
path('livreur/' , views.livreur , name='livreur'),
path('livraison_terminee/' , views.livraison_terminee , name='livraison_terminee'),
    path('modifier_produit/', views.modifier_produit, name='modifier_produit'),

    # Autres URLs de votre application
path('deconnexion/', views.deconnexion, name='deconnexion'),
path('profile/', views.profile, name='profile'),
path('profileliv/', views.profileliv, name='profileliv'),
path('profilepatient/', views.profilepatient, name='profilepatient'),
path('historique_pharmacie/', views.historique_pharmacie, name='historique_pharmacie'),
path('historique_livreur/', views.historique_livreur, name='historique_livreur'),
path('historique_patient', views.historique_patient, name='historique_patient'),

    path('api/produit/<int:produit_id>/', views.api_produit_detail, name='api_produit_detail'),
path('recherche-produit/' , views.recherche_produit , name='recherche-produit'),

path('envoyer_commande/', views.envoyer_commande, name='envoyer_commande'),
path('mes-commandes/', views.mes_commandes, name='mes_commandes'),
path('accepter_commande/<int:commande_id>/', views.accepter_commande, name='accepter_commande'),
path('product/<int:id_produit>/delete/', ProductDeleteView.as_view(), name='product-delete'),

path('admin/' , views.admin , name='admin'),
path('medecin/' , views.medecin , name='medecin'),
path('pharmacie/' , views.pharmacie , name='pharmacie'),
path('patient/' , views.patient, name='patient'),
path('pharmacie_details/<int:user_id>/', views.pharmacie_details, name='pharmacie_details'),
path('commandes-pharmacie/', views.commandes_pharmacie, name='commandes-pharmacie'),

path('footer', views.footer, name='footer'),
path('confirmationpharm/', views.confirmationpharm, name='confirmationpharm'),
path('checkoutout/', views.checkoutout, name='checkoutout'),
path('medecin_details/<int:medecin_id>/', views.medecin_details, name='medecin_details'),
path('ajouter_produit/', views.ajouter_produit, name='ajouter_produit'),



]