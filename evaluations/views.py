from django.shortcuts import render
from . import models

# Create your views here.


def all_evaluations(request):
    all_evaluations = models.Evaluations.objects.all()
    return render(
        request,
        "evaluations/home.html",
        context={
            "evaluations": all_evaluations,
        },
    )
