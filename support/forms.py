from django import forms
from django.utils.text import slugify
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
                    'content',
                    'region',
                    'age_group',
                    'type_of_request',
                )

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.topic)
        if commit:
            instance.save()
        return instance
