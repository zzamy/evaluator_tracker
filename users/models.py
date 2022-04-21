from django.contrib.auth.models import AbstractUser
from django.db import models
from core import models as core_models


# Create your models here.

class User(AbstractUser):
    NAME = models.CharField(max_length=30, blank=True)
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICE = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANG_KOR = "KOR"
    LANG_ENG = "ENG"
    LANG_CHOICE = (
        (LANG_KOR, "KOREAN"),
        (LANG_ENG, "ENGLISH"),
    )

    CURRENCY_USD = "USD"
    CURRENCY_KRW = "KWR"
    CURRENCY_CHOICE = (
        (CURRENCY_KRW, "KOREAN WON"),
        (CURRENCY_USD, "USD DOLLOR"),
    )

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

    site = models.CharField(choices=SITE_MAPPING, max_length=30, default=False)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANG_CHOICE, max_length=10, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICE, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)

    def __str__(self):
        return self.NAME
