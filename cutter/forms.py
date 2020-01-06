from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url']
        widgets = {
            'url':forms.TextInput(attrs={'class':'mb-2 form-control','placeholder':'Ingresa tu URL'})
        }