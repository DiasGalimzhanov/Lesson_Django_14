from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'color']
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control','id': 'validationCustom01', 'required': 'true', 'placeholder': 'Brand','style': 'width: 30rem;'}),
            'model': forms.TextInput(attrs={'class': 'form-control','id': 'validationCustom02', 'required': 'true', 'placeholder': 'Model','style': 'width: 30rem;'}),
            'year': forms.NumberInput(attrs={'class': 'form-control','id': 'validationCustom03', 'required': 'true', 'placeholder': 'Year','style': 'width: 30rem;'}),
            'color': forms.TextInput(attrs={'class': 'form-control','id': 'validationsCustom04', 'required': 'true', 'placeholder': 'Color','style': 'width: 30rem;'}),
        }

#style="width: 30rem;