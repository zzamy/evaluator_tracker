from django.urls import path
from evaluations import views as evaluation_views

app_name = "core"

urlpatterns = [path("", evaluation_views.all_evaluations, name="home")]
