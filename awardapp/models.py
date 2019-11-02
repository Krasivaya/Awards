from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from star_ratings.models import Rating

        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to = 'profile/', blank=True, default='profile/default.png')

    
class Projects(models.Model):
    project_title = models.CharField(max_length=255)
    project_image = models.ImageField(upload_to = 'images/', default='images/default.png')
    project_description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    author_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, default='1')
    link = models.URLField()
    country = CountryField(blank_label='(select country)', default='RW')