import django_filters  # Importation du module django_filters, qui fournit des fonctionnalités de filtrage
from .models import Commande  # Importation du modèle Commande depuis le module courant


# Définition d'un filtre personnalisé pour le modèle Commande
class CommandeFilter(django_filters.FilterSet):
    class Meta:
        model = Commande  # Spécification du modèle sur lequel le filtre sera appliqué

        # Définition des champs à inclure dans le filtre
        # Utilisation de '__all__' pour inclure tous les champs du modèle dans le filtre
        fields = '__all__'
        exclude = ['date_creation', 'client'] # Cette ligne exclut les champs date_creation et client du filtre. Les données de ces champs ne seront pas incluses dans les options de filtrage générées par le filtre.

        # En utilisant '__all__', tous les champs du modèle Commande seront inclus dans le filtre.
        # Cela signifie que le filtre généré contiendra des options pour filtrer les données
        # en fonction de toutes les colonnes de la table de la base de données associée au modèle Commande.
