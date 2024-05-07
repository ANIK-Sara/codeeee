from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User ,PharmaCommandes , Medecin , Pharmacie , Patient , Produit_Prescris , Ordonnance , Produit, Admin , Commande
# Register your models here.
admin.site.register(User),
admin.site.register(Medecin),
admin.site.register(Pharmacie),
admin.site.register(Patient),
admin.site.register(Admin),
admin.site.register(Produit),
admin.site.register(Commande),
admin.site.register(Produit_Prescris),
admin.site.register(Ordonnance),
admin.site.register(PharmaCommandes),