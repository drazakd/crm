from django.db import models
# Import des modèles nécessaires depuis d'autres applications
from client.models import Client
from produit.models import Produit

class Commande(models.Model):
    # Liste prédéfinie sous forme de tuple pour les états de la commande
    STATUS = (
        ('en instance', 'En instance'),
        ('non livré', 'Non livré'),
        ('livré', 'Livré')
    )

    # Définition des champs de la table Commande
    # Liaison avec le modèle Client
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    # Liaison avec le modèle Produit
    produit = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)
    # Champ pour enregistrer le statut de la commande
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    # Champ pour enregistrer la date de création de la commande
    date_creation = models.DateTimeField(auto_now_add=True, null=True)
