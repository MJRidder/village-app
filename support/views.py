from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Support


# Create your views here.
class SupportList(generic.ListView):
    queryset = Support.objects.all()
    template_name = "support_list.html"
