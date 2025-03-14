from django import forms
from .models import ContactForm


class ContactRequest(forms.ModelForm):
    """
    Form class for users to contact website owner
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = ContactForm
        fields = (
            'name',
            'topic',
            'email',
            'type_of_request',
            'message'
            )
