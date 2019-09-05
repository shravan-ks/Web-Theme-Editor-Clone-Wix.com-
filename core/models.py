from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
# Create your models here.
class notification(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/', blank=True, null=True, )
    date = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=1000)