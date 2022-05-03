from math import ceil
from django.shortcuts import render
from . import models

# Create your views here.


def all_evaluations(request):
    # Off set size modified
    page = int(request.GET.get("page", 1))
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    page_count = ceil(models.Evaluations.objects.count() / page_size)
    # it is manage 1 page details list no.
    all_evaluations = models.Evaluations.objects.all()[offset:limit]
    return render(
        request,
        "evaluations/home.html",
        context={
            "evaluations": all_evaluations,
            "page": page,
            "page_count": page_count,
            "page_range": range(0, page_count),
        },
    )
