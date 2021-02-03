from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class logger(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    occupation = models.CharField(max_length=30)
    profile = models.ImageField(null=True, blank= True, upload_to = 'images/' )
    email = models.EmailField( max_length=254)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=True)
    
   
    def __str__(self):
        return self.first_name
        
    

class article(models.Model):
    
    title = models.CharField(max_length=190)
    author = models.ForeignKey(User, on_delete= models.CASCADE )
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title + " " + '\t' + '\t' + " " + str(self.date.strftime('%Y-%m-%d')) + " " + '\t' + '\t' + " " + str(self.author)
    
