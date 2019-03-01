
from django.db import models

from ckeditor.fields import RichTextField

class Slider(models.Model):
    header = models.CharField(max_length = 80, blank = True, null = True)
    description = models.CharField(max_length = 200, blank = True, null = True)
    sliderImage = models.ImageField(upload_to = 'images/', blank = True, null = True)

    def __str__(self):
        return self.header


class aboutUs(models.Model):
    description = models.CharField(max_length = 200, blank = True, null = True)

class belowAboutUs(models.Model):
    header = models.CharField(max_length = 100, blank = True, null = True)
    text = models.TextField(max_length = 500, blank = True, null = True)

class callToAction(models.Model):
    header = models.CharField(max_length = 100, blank = True, null = True)
    description = models.CharField(max_length = 300, blank = True, null = True)
    link = models.URLField(max_length = 200, blank = True, null = True)

class skillsDescription(models.Model):
    description = models.CharField(max_length = 300, blank = True, null = True)

class Skill(models.Model):
    skillName = models.CharField(max_length = 150, blank = True, null = True)
    skillPercentage = models.IntegerField(blank = True, null = True)

""" Implement portfolio """

class teamDescription(models.Model):
    description = models.CharField(max_length = 300, blank = True, null = True)

class team(models.Model):
    name = models.CharField(max_length = 25, blank = True, null = True)
    title = models.CharField(max_length = 20, blank = True, null = True)
    image = models.ImageField(upload_to = 'images/', blank = True, null = True)

class contactDescription(models.Model):
    description = models.CharField(max_length = 150, blank = True, null = True)

class contact(models.Model):
    icon = models.CharField(max_length = 200, blank = True, null = True)
    header = models.CharField(max_length = 30, blank = True, null = True)
    content = models.CharField(max_length = 150, blank = True, null = True)

