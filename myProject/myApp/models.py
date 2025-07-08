from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customeUser(AbstractUser):
    GENDER =[
        ('male','Male'),
        ('female','Female'),
        ('others','Others'),
    ]
    
    USER =[
        ('viewers','Viewers'),
        ('bloger','Bloger'),
    ]
    user_type = models.CharField(max_length=20, choices=USER, null=True)
    gender = models.CharField(choices=GENDER,  max_length=20, null=True)
    age = models.PositiveIntegerField(null=True)
    contact_no = models.CharField(max_length=100, null=True)
    profile_pic = models.ImageField(upload_to='Media/profile_pic', null=True)
    
    
    def __str__(self):
        return f"{self.username}-{self.age}"
    


class viewersProfileModel(models.Model):
    PREFFERED_CONTENT = [
        ('articles', 'Articles'),
        ('videos', 'Videos'),
        ('podcast', 'both')
    ]
    
    user = models.OneToOneField(customeUser, on_delete=models.CASCADE, related_name='viewersProfile')
    Bio=models.TextField(max_length=100,null=True)
    interests = models.CharField(max_length=255, blank=True, null=True) 
    preferred_content_type = models.CharField(max_length=100, choices=PREFFERED_CONTENT, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.user.username}"


class blogerProfileModel(models.Model):
    user = models.OneToOneField(customeUser, on_delete=models.CASCADE, related_name= 'blogersProfile')
    bio = models.TextField(max_length=200, null=True)
    website_url = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.user.username}"