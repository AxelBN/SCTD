from django import forms
from .models import TrackDocument


class TrackTrack(forms.ModelForm):
    class Meta:
        model = TrackDocument
        fields = '__all__'
