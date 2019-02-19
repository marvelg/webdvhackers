
from django.db import models

from ckeditor.fields import RichTextField

class Slider(models.Model):
    header = models.CharField(max_length = 80)
    description = models.CharField(max_length = 200)
    sliderImage = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.header
class belowSlider(models.Model):
    pass

class aboutUs(models.Model):
    description = models.CharField(max_length = 200)

class belowAboutUs(models.Model):
    header = models.CharField(max_length = 100)
    text = models.TextField(max_length = 500)

class callToAction(models.Model):
    header = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)
    link = models.URLField(max_length = 200)

class skillsDescription(models.Model):
    description = models.CharField(max_length = 300)

class skill(models.Model):
    skillName = models.CharField(max_length = 150)
    skillPercentage = models.IntegerField()

""" Implement the Facts section """
class factsDescription(models.Model):
    description = models.CharField(max_length = 200)

class Fact(models.Model):
    header = models.CharField(max_length = 50)
    number = models.IntegerField()



