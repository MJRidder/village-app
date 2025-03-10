from django.shortcuts import render, reverse
from django.views import generic
from .models import Faq


def frequently_asked_questions(request):
    """
    Renders the FAQ page with answers
    """
    faq = Faq.objects.all().order_by('question').first()

    return render(
        request,
        "faq/frequently_asked_questions.html",
        {"faq": faq},
    )


class FaqList(generic.ListView):
    queryset = Faq.objects.all().order_by('priority').first()
    template_name = "faq/frequently_asked_questions.html"
    paginate_by = 10
