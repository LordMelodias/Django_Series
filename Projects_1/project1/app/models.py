from django.db import models

# Create your models here.
class userProfile(models.Model):
    username = models.CharField(max_length = 255, unique=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, unique=True, null=True, blank=True)
    password = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    
    def __str__(self):
        return self.username