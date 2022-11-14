from django import forms
from .models import Site

class SiteSite(forms.ModelForm):
    class Meta:
        model = Site
        fields = '__all__'