from django.shortcuts import render
from .models import About


def about_village(request):
    """
    Renders the About Village page
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
