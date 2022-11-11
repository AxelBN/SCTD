from django import forms
from .models import Delivery


class dato(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'
