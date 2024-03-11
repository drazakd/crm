from django.forms import ModelForm
from .models import Commande # le formulaire sera relié a Commande

#relier le formulaire au model
class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'
