from django import forms
from .models import Dogz

class DogzForm(forms.ModelForm):
    class Meta:
        model = Dogz
        fields = [

            'nome',
            'raca',
            'obs',
            'site',
        ]