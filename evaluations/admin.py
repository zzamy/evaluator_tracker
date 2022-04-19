from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Evaluations)
class EvaluationsAdmin(admin.ModelAdmin):
    """Custom Evaluation Admin"""
    list_display = (
        "Enquiry_Date",
        "Location",
        "Evaluator",
        "Enquiry_Source",
        "Place",
        "REG_No",
        "Status",
        "RF",
        "Quoted_Price",
        "Expected_Price",
        "Final_Price",
        "Brand",
        "Varient",
        "Y_O_M",
        "KMs",
    )