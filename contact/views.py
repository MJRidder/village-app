from django.shortcuts import render
from django.contrib import messages
from .models import ContactForm
from.forms import ContactRequest


def contact(request):
    """
    Display the page where a user can contact the
    website owner
    :model:`contact.ContactForm`.

    **Context**

    ``contact``
        An instance of :model:`contact.ContactForm`.

    **Template:**

    :template:`contact/contact.html`
    """
    if request.method == "POST":
        contact_form = ContactRequest(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your message has been received! We hope to get '
                'back to you as soon as possible!'
            )
    contact_form = ContactRequest()

    return render(
        request,
        "contact/contact.html",
        {
            "contact_form": contact_form
        })
