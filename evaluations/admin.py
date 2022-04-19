from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Evaluations)
class EvaluationsAdmin(admin.ModelAdmin):
    pass

