from django.shortcuts import render, HttpResponse, redirect
from .forms import CommandeForm
from .models import Commande

# Vue pour afficher la liste des commandes
def list_commande(request):
    # Ici, vous pourriez récupérer les commandes depuis la base de données
    # et les passer au template pour les afficher
    return render(request, 'commande/list_commande.html')

# Vue pour ajouter une nouvelle commande
def ajouter_commande(request):
    # Créer une instance de CommandeForm (un formulaire Django)
    form = CommandeForm()

    # Vérifier si la méthode de requête est POST (l'utilisateur a soumis le formulaire)
    if request.method == 'POST':
        # Créer une instance de CommandeForm avec les données POST reçues
        form = CommandeForm(request.POST)
        # Vérifier si le formulaire est valide
        if form.is_valid():
            # Sauvegarder les données du formulaire dans la base de données
            form.save()
            # Rediriger l'utilisateur vers la page d'accueil après avoir ajouté la commande
            return redirect('/')

    # Préparer le contexte avec le formulaire à afficher dans le template
    context = {'form': form}
    # Renvoyer la page du formulaire avec le contexte
    return render(request, 'commande/ajouter_commande.html', context)

# Vue pour modifier une commande existante
def modifier_commande(request, pk):
    # Récupérer la commande spécifique en fonction de la clé primaire (id)
    commande = Commande.objects.get(id=pk)
    # Créer une instance de CommandeForm avec les données de la commande à modifier
    form = CommandeForm(instance=commande)

    # Vérifier si la méthode de requête est POST (l'utilisateur a soumis le formulaire de modification)
    if request.method == 'POST':
        # Mettre à jour l'instance du formulaire avec les données POST reçues
        form = CommandeForm(request.POST, instance=commande)
        # Vérifier si le formulaire est valide
        if form.is_valid():
            # Sauvegarder les modifications dans la base de données
            form.save()
            # Rediriger l'utilisateur vers la page d'accueil après avoir modifié la commande
            return redirect('/')

    # Préparer le contexte avec le formulaire à afficher dans le template
    context = {'form': form}
    # Renvoyer la page du formulaire avec le contexte
    return render(request, 'commande/ajouter_commande.html', context)

# Vue pour supprimer une commande existante
def supprimer_commande(request,pk):
    commande = Commande.objects.get(id=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('/')
    context = {'item': commande}
    # Cette vue rend simplement le modèle de la page de suppression de commande.
    return render(request, 'commande/supprimer_commande.html', context)
