from django.shortcuts import render
from .models import Client
from commande.filters import CommandeFilter

def list_client(request, pk):
    # Récupérer le client en fonction de son ID
    client = Client.objects.get(id=pk)

    # Récupérer toutes les commandes associées à ce client
    commande = client.commande_set.all()

    # Compter le nombre total de commandes pour ce client
    commande_total = commande.count()

    # Initialiser le filtre de commande avec les données de requête et le queryset de commandes
    myFilter = CommandeFilter(request.GET, queryset=commande)

    # Appliquer le filtre et obtenir le queryset filtré
    commande = myFilter.qs

    # Préparer le contexte à envoyer au template
    context = {
        'client': client,                # Client concerné
        'commande': commande,           # Liste des commandes filtrées
        'commande_total': commande_total,  # Nombre total de commandes
        'myFilter': myFilter             # Instance du filtre de commande
    }

    # Rendre le template 'list_client.html' avec le contexte fourni
    return render(request, 'client/list_client.html', context)
