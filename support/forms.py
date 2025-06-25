from django import forms
from django.utils.text import slugify
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
        date = forms.DateField(
            widget=forms.DateInput(attrs={'type': 'date'})
        )

# added date to the slugify to make the slug field unique
# "Unique=True" removed from model as topic duplication is OK
# review if PostID is a possibility instead of date
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.topic.date)
        if commit:
            instance.save()
        return instance
