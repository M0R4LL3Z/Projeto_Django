from django import forms
from .models import Estudante,Curso

class Estudante(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = ['nome', 'data_de_nascimento','email'] 

class Curso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['curso', 'professor','data_inicio','data_termino'] 
