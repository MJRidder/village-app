from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Support


class SupportList(generic.ListView):
    queryset = Support.objects.all().filter(status=1)
    template_name = "support/index.html"
    paginate_by = 12


def support_detail(request, slug):
    """
    Display an individual :model:`support.Support`.

    **Context**

    ``support``
        An instance of :model:`support.Support`.

    **Template:**

    :template:`support/support_detail.html`
    """

    queryset = Support.objects.filter(status=1)
    supportPage = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "support/support_detail.html",
        {"support": supportPage},
    )
