from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta :
        abstract = True