from django.conf import settings
from django.db import models

# Create your models here.
class theme1(models.Model):
    type = models.CharField(max_length=50, default='Normal Theme',)
    projectname = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=50)
    menu1 = models.CharField(max_length=25, blank=True)
    menu2 = models.CharField(max_length=25, blank=True,)
    menu3 = models.CharField(max_length=25,  blank=True,)
    menu4 = models.CharField(max_length=25, blank=True,)
    brandimg = models.ImageField(upload_to='images/', blank=True, null=True,)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


