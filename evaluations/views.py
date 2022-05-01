from django.shortcuts import render
from . import models

# Create your views here.


def all_evaluations(request):
    all_evaluations = models.Evaluations.objects.all()
    return render(
        request,
        "all_evaluations.html",
        context={
            "evaluations": all_evaluations,
        },
    )
