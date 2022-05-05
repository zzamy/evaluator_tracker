from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

# Create your views here.


def all_evaluations(request):
    # Off set size modified
    page = request.GET.get("page", 1)
    evaluation_list = models.Evaluations.objects.all()
    paginator = Paginator(evaluation_list, 10)
    evaluationss = paginator.get_page(page)
    print(vars(evaluationss.paginator))

    return render(
        request,
        "evaluations/home.html",
        context={"evaluations": evaluationss},
    )
