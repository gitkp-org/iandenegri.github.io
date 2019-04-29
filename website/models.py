from django.db import models

# Create your models here.

class Socials(models.Model):
    social_site = models.CharField()
    url = models.URLField()
    image = models.ImageField()