from django.urls import path
from evaluations import views as evaluation_views

urlpatterns = [
    path("", evaluation_views.all_evaluations),
]
