from django.shortcuts import render
from django.http import HttpResponse
#import du model commande
from commande.models import Commande
from client.models import Client

# Create your views here.
def home(request):
    commandes = Commande.objects.all() # requete pour faire appel a toutes les commandes
    clients = Client.objects.all()
    # je mets tout dans un dictionnaire qu'on va appeler context qui va se charger de renvoyer tout ca
    context = {'commandes':commandes,'clients':clients}
    return render(request,'produit/accueil.html',context) # ensuite mettre le dictionnaire context dans render