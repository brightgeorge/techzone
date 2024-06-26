from django.db import models

# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length=200)
    prof = models.TextField()
    mob = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250)
    facebook_endis = models.CharField(max_length=250)
    instagram = models.CharField(max_length=250)
    instagram_endis = models.CharField(max_length=250)
    linkedin = models.CharField(max_length=250)
    linkedin_endis = models.CharField(max_length=250)
    twitter = models.CharField(max_length=250)
    twitter_endis = models.CharField(max_length=250)
    prof_details = models.TextField()
    our_services = models.CharField(max_length=250)

    profile_image = models.ImageField(upload_to='images/')


class client_services(models.Model):
    service_name = models.CharField(max_length=200)
    flag = models.CharField(max_length=200)

class images_profile(models.Model):
    profile_name = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='images/')