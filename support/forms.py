from django import forms
from .models import Respond, Support


class RespondForm(forms.ModelForm):
    class Meta:
        model = Respond
        fields = ('body',)


class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = (
                    'topic',
                    'slug',
                    'parent',
                    'content',
                    # 'created_on',
                    # 'updated_on',
                    'region',
                    'age_group',
                    'type_of_request',
                    'status',
                )
