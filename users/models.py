from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import CharField


# Create your models here.

class User(AbstractUser):

    SITE_CHENNAI1 = "HMP Chennai"
    SITE_CHENNAI2 = "Chennai-TVS"
    SITE_DELHI1 = "Allied Gurgaon"
    SITE_DELHI2 = "Allied Noida"
    SITE_DELHI3 = "Dhingra Gurgaon"
    SITE_DELHI4 = "Dhingra Faridabad"
    SITE_DELHI5 = "Lohia Peeragarhi"
    SITE_DELHI6 = "Lohia Wazirpur"
    SITE_DELHI7 = "Lohia Noida"
    SITE_MUMBAI1 = "Mumbai"
    SITE_AP1 = "Salem-TVS"
    SITE_AP2 = "Erode-TVS"
    SITE_AP3 = "Coimbatore-TVS"
    SITE_AP4 = "Secunderabad-TVS"
    SITE_AP5 = "Vijayawada-TVS"
    SITE_AP6 = "Erode/Salem-TVS"
    SITE_AP7 = "Hyderabad-TVS"
    SITE_AP8 = "Visakhapatnam-TVS"
    SITE_AP9 = "Madurai-TVS"

    SITE_MAPPING = (
        (SITE_CHENNAI1, "HMP Chennai"),
        (SITE_CHENNAI2, "Chennai-TVS"),
        (SITE_DELHI1, "Allied Gurgaon"),
        (SITE_DELHI2, "Allied Noida"),
        (SITE_DELHI3, "Dhingra Gurgaon"),
        (SITE_DELHI4, "Dhingra Faridabad"),
        (SITE_DELHI5, "Lohia Peeragarhi"),
        (SITE_DELHI6, "Lohia Wazirpur"),
        (SITE_DELHI7, "Lohia Noida"),
        (SITE_MUMBAI1, "Mumbai"),
        (SITE_AP1, "Salem-TVS"),
        (SITE_AP2, "Erode-TVS"),
        (SITE_AP3, "Coimbatore-TVS"),
        (SITE_AP4, "Secunderabad-TVS"),
        (SITE_AP5, "Vijayawada-TVS"),
        (SITE_AP6, "Erode/Salem-TVS"),
        (SITE_AP7, "Hyderabad-TVS"),
        (SITE_AP8, "Visakhapatnam-TVS"),
        (SITE_AP9, "Madurai-TVS"),
    )

    name = models.CharField(max_length=50, null = True)
    site = models.CharField(choices=SITE_MAPPING, max_length=30, default=False)