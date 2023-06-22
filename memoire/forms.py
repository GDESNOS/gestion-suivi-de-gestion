from django.forms import ModelForm
from django import forms
#from memoire.models import  Contacter
from memoire.models import *



class ProjetForm(forms.Form):
    class Meta:
        model=Project
        fields='__all__'
    
"""  
class ContacterForm(forms.ModelForm):
    class Meta:
        model=Contacter
        fields='__all__' """

# Ma classe qui l'envoie des fichiers 

class MyForm(forms.ModelForm):
    class Meta:
        model=MyModel
        fields='__all__'