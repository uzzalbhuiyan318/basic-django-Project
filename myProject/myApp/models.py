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