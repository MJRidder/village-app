from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Support


# Create your views here.
class SupportList(generic.ListView):
    queryset = Support.objects.all().filter(status=1)
    template_name = "support/index.html"
    paginate_by = 6
