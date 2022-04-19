from multiprocessing.sharedctypes import Value
from django.db import models
from core import models as core_models
from users import models as user_models

# Create your models here.

class Evaluations(core_models.TimeStampedModel):
    Enquiry_Date = models.DateTimeField(auto_now_add=True)

    Location = models.ForeignKey("users.Site", on_delete=models.CASCADE, null=True)


    Evaluator = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)


    Source1 = "Out-bound"
    Source2 = "Exchange(Trade-in)"
    Source3 = "Workshop"

    Source_Mapping = (
        (Source1, "Out-bound"),
        (Source2, "Exchange(Trade-in)"),
        (Source3, "Workshop"),
    )

    Enquiry_Source = models.CharField(choices=Source_Mapping, max_length=30)

    Place1 = "Showroom"
    Place2 = "Field"

    Place_Mapping = (
        (Place1, "Showroom"),
        (Place2, "Field"),
    )

    Place = models.CharField(choices=Place_Mapping, max_length=30)

    REG_No = models.CharField(max_length=10)

    Status1 = "Enquiry"
    Status2 = "Follow-up"
    Status3 = "Evaluated"
    Status4 = "Quotation"
    Status5 = "Booked"
    Status6 = "Procured"
    Status7 = "Failed"

    Status_Mapping = (
        (Status1, "Enquiry"),
        (Status2, "Follow-up"),
        (Status3, "Evaluated"),
        (Status4, "Quotation"),
        (Status5, "Booked"),
        (Status6, "Procured"),
        (Status7, "Failed"),
    )

    Status = models.CharField(choices=Status_Mapping, max_length=30)

    RF = models.CharField(max_length=30)

    Quoted_Price = models.IntegerField()
    Expected_Price = models.IntegerField()

    #Different = 
    Final_Price = models.IntegerField(null=True)
    Brand = models.CharField(max_length=30)
    Varient = models.CharField(max_length=30)
    Y_O_M = models.DateField()
    KMs = models.IntegerField()

    



