from django.db import models
from django.conf import settings


# Create your models here.
class resumeDb(models.Model):
    Project_Name = models.CharField(max_length=50, unique=True,)
    Profile_Name = models.CharField(max_length=50,)
    Address = models.CharField(max_length=255, blank=True,null=True,)
    Phone_Number = models.CharField(max_length=10, blank=True,null=True,)
    Email = models.EmailField(max_length=50, blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Type = models.CharField(max_length=50, default='Resume')
#     second form
    About_Me = models.CharField(max_length=2000, blank=True, null=True)
    Skills = models.CharField(max_length=1000,blank=True,null=True)
    Experience = models.CharField(max_length=1000, blank=True,null=True)
    Upload_Resumne = models.FileField(upload_to='files/', blank=True, null=True,)
    Profile_Picture = models.ImageField(upload_to='images/', blank=True, null=True, )
#   socail and tools
    Facebook = models.CharField(max_length=100, blank=True, null=True)
    Instagram = models.CharField(max_length=100, blank=True, null=True)
    Twitter = models.CharField(max_length=100, blank=True, null=True)
    GitHub = models.CharField(max_length=100, blank=True, null=True)
#   colors cutomomize
    Background_Color_Left_Column = models.CharField(max_length=10,blank=True, null=True)
    Background_Color_Right_Column = models.CharField(max_length=10, blank=True, null=True)
    Accent_Color = models.CharField(max_length=10, blank=True, null=True)