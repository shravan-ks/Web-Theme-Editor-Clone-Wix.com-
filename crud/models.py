from django.db import models


# Create your models here.
class crud(models.Model):
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=40)
