from django.db import models
from .project import getToken, getWLANData
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class loginDetails(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    subwayAccount = models.BooleanField(default=True)


class profile(models.Model):
     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     subwayAccount = models.BooleanField(default=True)
     busAccount = models.BooleanField(default=True)
     def __str__(self):
        return f"{self.user.username}"

class checkboxModel(models.Model):
    token = getToken()
    
    wlanName =  models.CharField(max_length=255, default="Emergency_Test")
    stationName =  models.CharField(max_length=255, default="Subway Toggle")
    
    isChecked = models.BooleanField(null=True,blank=True)
    isSubwayWlan= models.BooleanField(default=True)


    def __str__(self):
        return f"{self.stationName}"
