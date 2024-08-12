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


    whatsapp = models.CharField(max_length=250)
    whatsapp_endis = models.CharField(max_length=250)
    youtube = models.CharField(max_length=250)
    youtube_endis = models.CharField(max_length=250)
    google = models.CharField(max_length=250)
    google_endis = models.CharField(max_length=250)
    telegram = models.CharField(max_length=250)
    telegram_endis = models.CharField(max_length=250)

    genaral_link_name = models.CharField(max_length=250)
    genaral_link = models.CharField(max_length=250)
    genaral_link_endis = models.CharField(max_length=250)

    genaral_link_name2 = models.CharField(max_length=250)
    genaral_link2 = models.CharField(max_length=250)
    genaral_link_endis2 = models.CharField(max_length=250)

    genaral_link_name3 = models.CharField(max_length=250)
    genaral_link3 = models.CharField(max_length=250)
    genaral_link_endis3 = models.CharField(max_length=250)

    prof_details = models.TextField()
    our_services = models.CharField(max_length=250)

    profile_image = models.ImageField(upload_to='images/')
    profile_image_back = models.ImageField(upload_to='background/')
    brochure = models.ImageField(upload_to='brochures/')


class client_services(models.Model):
    service_name = models.CharField(max_length=200)
    flag = models.CharField(max_length=200)

class images_profile(models.Model):
    profile_name = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='images/')