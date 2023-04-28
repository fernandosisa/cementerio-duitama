from django import forms
from .models import Task
from .models import Propietario
from .models import FamiliarDifunto


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a title'}),
            'description':  forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a description'}),
            'important':  forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }


class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombresCompletos', 'telefono',
                  'telefonoAuxiliar', 'direccion', 'ciudad']
        widgets = {
            'nombresCompletos':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe los nombres completos'}),
            'telefono':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el telefono'}),
            'telefonoAuxiliar':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el telefono Auxiliar'}),
            'direccion':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la direccion'}),
            'ciudad':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la ciudad'}),
        }


class FamiliarDifuntoForm(forms.ModelForm):
    class Meta:
        model = FamiliarDifunto
        fields = ['nombresCompletos', 'telefono',
                  'telefonoAuxiliar', 'direccion', 'ciudad']
        widgets = {
            'nombresCompletos':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe los nombres completos'}),
            'telefono':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el telefono'}),
            'telefonoAuxiliar':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el telefono Auxiliar'}),
            'direccion':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la direccion'}),
            'ciudad':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la ciudad'}),
        }
