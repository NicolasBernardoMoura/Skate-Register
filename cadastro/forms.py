from django import forms
from .models import Skatista

class SkatistaForm(forms.ModelForm):

    class Meta:
        model = Skatista
        fields = '__all__'

        widgets = {

            'nome': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'idade': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'cidade': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'modalidade': forms.Select(attrs={
                'class': 'form-select'
            }),

            'nivel': forms.Select(attrs={
                'class': 'form-select'
            }),

            'foto': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),

        }