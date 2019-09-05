from django.conf import settings
from django.db import models

# Create your models here.
class feedbackform(models.Model):
    Subject = models.CharField(max_length=300, null=True)
    Your_Message = models.CharField(max_length=3000,)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Created = models.DateTimeField(auto_now_add=True, blank=True,null=True)