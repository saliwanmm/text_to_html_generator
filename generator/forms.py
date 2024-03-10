from django import forms
from .models import GeneratorModel


class GeneratorForm(forms.ModelForm):
    class Meta:
        model = GeneratorModel
        fields = ["title", "description"]