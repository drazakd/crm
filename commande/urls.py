from django.urls import path
from . import views

# Définition des URL (chemins) de l'application "commande"
urlpatterns = [
    # Chemin vers la page d'accueil des commandes
    path('', views.list_commande),  # Lien direct vers la vue list_commande de views.py

    # Chemin pour ajouter une nouvelle commande
    path('ajout_commande/', views.ajouter_commande, name='ajout_commande'),
    # Lorsque cette URL est accédée, elle appelle la vue ajouter_commande de views.py et
    # lui donne le nom 'ajout_commande' pour l'utiliser dans les templates Django

    # Chemin pour modifier une commande existante
    path('modifier_commande/<str:pk>', views.modifier_commande, name='modifier_commande'),
    # Lorsque cette URL est accédée avec un identifiant de commande spécifique (pk),
    # elle appelle la vue modifier_commande de views.py et lui donne le nom 'modifier_commande'
    # pour l'utiliser dans les templates Django.
    # Le paramètre <str:pk> permet de capturer l'identifiant de la commande à modifier.

    # Chemin pour supprimer une commande existante
    path('supprimer_commande/<str:pk>', views.supprimer_commande, name='supprimer_commande')
    # Lorsque cette URL est accédée avec un identifiant de commande spécifique (pk),
    # elle appelle la vue supprimer_commande de views.py et lui donne le nom 'supprimer_commande'
    # pour l'utiliser dans les templates Django.
    # Le paramètre <str:pk> permet de capturer l'identifiant de la commande à supprimer.
]
