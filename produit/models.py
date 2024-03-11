from django.db import models

# Create your models here.
class Tag(models.Model):
    nom = models.CharField(max_length=200,null=True)
    #pour afficher les noms du tag
    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=200,null=True)
    prix = models.FloatField(null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)

    # creation de champ appelé tag qui pointera vers un models appelé Tag la class Tag
    tag = models.ManyToManyField(Tag)

    #pour afficher les noms sur les produits
    def __str__(self):
        return self.nom