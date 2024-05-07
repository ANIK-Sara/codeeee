from django.urls import path 
from . import views
urlpatterns = [
path('' , views.index , name='index'),
path('login/' , views.login_view , name='login_view'),
path('register/' , views.register , name='register'),
path('admin/' , views.admin , name='admin'),
path('medecin/' , views.medecin , name='medecin'),
path('pharmacie/' , views.pharmacie , name='pharmacie'),
path('patient/' , views.patient, name='patient'),
path('pharmacies_details/<int:pharmacie_id>/', views.pharmacie_details, name='pharmacie_details'),
path('footer', views.footer, name='footer'),
path('confirmationpharm/', views.confirmationpharm, name='confirmationpharm'),
path('checkoutout/', views.checkoutout, name='checkoutout'),
path('medecin_details/<int:medecin_id>/', views.medecin_details, name='medecin_details'),



]