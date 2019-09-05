from django.conf import settings
from django.db import models

# Create your models here.
class CompanyDb(models.Model):
    Project_Name = models.CharField(max_length=50, unique=True,)
    Brand_Name = models.CharField(max_length=50,)
    Address = models.CharField(max_length=255, blank=True,null=True,)
    Phone_Number = models.CharField(max_length=10, blank=True,null=True,)
    Email = models.EmailField(max_length=50, blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Type = models.CharField(max_length=50, default='Company Theme')
#     second form
    Brand_Logo = models.ImageField(upload_to='images/', blank=True, null=True, )
    Banner_Heading = models.CharField(max_length=200, blank=True, null=True)
    Banner_Text= models.CharField(max_length=1000,blank=True,null=True)
    Our_Services = models.CharField(max_length=1000, blank=True,null=True)
    About_Us = models.CharField(max_length=2000,blank=True,null=True)
#   socail and tools
    Facebook = models.CharField(max_length=100, blank=True, null=True)
    Instagram = models.CharField(max_length=100, blank=True, null=True)
    Twitter = models.CharField(max_length=100, blank=True, null=True)
#   colors cutomomize
    Background_Color_Banner = models.CharField(max_length=10,blank=True, null=True)
    Background_Color_Service = models.CharField(max_length=10, blank=True, null=True)
    Background_Color_About = models.CharField(max_length=10, blank=True, null=True)
    Background_Color_Navbar = models.CharField(max_length=10, blank=True, null=True)
    Accent_Color = models.CharField(max_length=10, blank=True, null=True)

