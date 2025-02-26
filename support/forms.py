from django import forms
from .models import Respond


class RespondForm(forms.ModelForm):
    class Meta:
        model = Respond
        fields = ('body',)