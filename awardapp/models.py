from django.db import models
from django.contrib.auth.models import User

        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to = 'profile/', blank=True, default='profile/default.png')

      