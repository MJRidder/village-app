from django.shortcuts import render, reverse
from django.views import generic
from .models import Faq


class FaqList(generic.ListView):
    queryset = Faq.objects.all()
    template_name = "faq/faq.html"
    paginate_by = 10
