from django.conf import settings
from django.db import models


# Create your models here.
from django.utils.safestring import mark_safe


class RestDb(models.Model):
    projectname = models.CharField(max_length=50,unique=True,)
    brandname = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Type = models.CharField(max_length=50, default='Restaurant')
    Created = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    brandimg = models.ImageField(upload_to='images/', blank=True, null=True, )
    about = models.CharField(max_length=5000)
    ph_num = models.CharField(max_length=10)
    review_link = models.CharField(max_length=1000)
    gallery1 = models.ImageField(upload_to='images/', blank=True, null=True, )
    gallery2 = models.ImageField(upload_to='images/', blank=True, null=True, )
    gallery3 = models.ImageField(upload_to='images/', blank=True, null=True, )
    gallery4 = models.ImageField(upload_to='images/', blank=True, null=True, )
    gallery5 = models.ImageField(upload_to='images/', blank=True, null=True, )
    gallery6 = models.ImageField(upload_to='images/', blank=True, null=True, )
    gallery7 = models.ImageField(upload_to='images/', blank=True, null=True, )
    gallery8 = models.ImageField(upload_to='images/', blank=True, null=True, )
    menu =models.FileField(upload_to='files/', blank=True, null=True,)
    address = models.CharField(max_length=3000)
    maps = models.CharField(max_length=5000)
#     tools
    favicon = models.ImageField(upload_to='images/', blank=True, null=True, )
    AppIcon = models.ImageField(upload_to='images/', blank=True, null=True, )
#     tools seo
    title = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=150 , blank=True, null=True)
#     social
    Facebook = models.CharField(max_length=100, blank=True, null=True)
    Instagram = models.CharField(max_length=100, blank=True, null=True)
    Twitter = models.CharField(max_length=100, blank=True, null=True)
    # social title
    Social_Title = models.CharField(max_length=100, blank=True, null=True)
    Social_Image = models.ImageField(upload_to='images/', blank=True, null=True, )
    Social_Description = models.CharField(max_length=150 , blank=True, null=True)


class RestDbContact(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True)
    Email = models.CharField(max_length=100, blank=True, null=True)
    Your_Message = models.CharField(max_length=3000 , blank=True, null=True)
    theme = models.ForeignKey(RestDb, on_delete=models.CASCADE, default=7)