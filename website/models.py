from django.db import models
from PIL import Image

# Create your models here.

class Social(models.Model):
    social_site = models.CharField(max_length=128)
    url = models.CharField(max_length=128)
    image = models.ImageField(upload_to="social_icons")

    def __str__(self):
        return self.social_site


class WebsiteSection(models.Model):
    section_name = models.CharField(max_length=128)
    section_blurb = models.TextField()

    def __str__(self):
        return self.section_name

class Project(models.Model):
    project_name = models.CharField(max_length=128)
    URL = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.project_name

class Interest(models.Model):
    interest_name = models.CharField(max_length=128)

    def __str__(self):
        return self.interest_name

class Owner(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    resume = models.FileField(upload_to='documents/')

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)
