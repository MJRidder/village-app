from django.shortcuts import render
from .models import ContactForm


def contact(request):
    context = {'title': 'Hello, World'}
    return render(request, 'contact/contact.html', context)
