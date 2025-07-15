from django import forms
from .models import Respond, Support


class RespondForm(forms.ModelForm):
    class Meta:
        model = Respond
        fields = ('body',)


class SupportForm(forms.ModelForm):
    # added date field to the SupportForm [CHECK REQUIRED]
    class Meta:
        model = Support
        fields = (
                    'topic',
                    'content',
                    'region',
                    'age_group',
                    'type_of_request',
                )
