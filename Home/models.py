
from django.db import models

from ckeditor.fields import RichTextField

class Slider(models.Model):
    header = models.CharField(max_length = 80, blank = True, null = True)
    description = models.CharField(max_length = 200, blank = True, null = True)
    sliderImage = models.ImageField(upload_to = 'images/', null = True)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name_plural = "1.1 Sliders"

class aboutUs(models.Model):
    description = models.CharField(max_length = 200, blank = True, null = True)

    def __str__(self):
        return "About Us"

    class Meta:
        verbose_name_plural = "1.2 AboutUs"

class belowAboutUs(models.Model):
    icon = models.CharField(max_length = 50 , blank = True, null = True)
    image = models.ImageField(upload_to = 'images/', null = True)
    header = models.CharField(max_length = 100, blank = True, null = True)
    text = models.TextField(max_length = 500, blank = True, null = True)
    
    def __str__(self):
        return self.header

    class Meta:
        verbose_name_plural = "1.3 BelowAboutUs"

class callToAction(models.Model):
    header = models.CharField(max_length = 100, blank = True, null = True)
    description = models.CharField(max_length = 300, blank = True, null = True)
    link = models.URLField(max_length = 200, blank = True, null = True)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name_plural = "1.4 Calltoaction"

class skillsDescription(models.Model):
    description = models.CharField(max_length = 300, blank = True, null = True)

    class Meta:
        verbose_name_plural = "1.5 SkillsDescription"

class Skill(models.Model):
    skillName = models.CharField(max_length = 150, blank = True, null = True)
    skillPercentage = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return self.skillName

    class Meta:
        verbose_name_plural = "2.1 Skill"

class portfolioCategories(models.Model):
    category = models.CharField(max_length = 50, blank = True, null = True)

    def __str__(self):
        return self.category

    def exactCategory(self):
        category = self.category
        return category.replace(" ", "").upper()

    class Meta:
        verbose_name_plural = "2.2 PortfolioCategories"

class Project(models.Model):
    projectImage = models.ImageField(upload_to = 'images/', null = True)
    projectName = models.CharField(max_length = 150, blank = True, null = True)
    projectCategory = models.CharField(max_length = 50, blank = True, null = True)

    def __str__(self):
        return self.projectName

    def exactCategory(self):
        projectCategory = self.projectCategory
        return projectCategory.replace(" ", "").upper()

    class Meta:
        verbose_name_plural = "2.3 Projects"

class teamDescription(models.Model):
    description = models.CharField(max_length = 300, blank = True, null = True)

    def __str__(self):
        return "Team Description"

    class Meta:
        verbose_name_plural = "2.4 TeamDescription"

class Team(models.Model):
    name = models.CharField(max_length = 25, blank = True, null = True)
    title = models.CharField(max_length = 20, blank = True, null = True)
    image = models.ImageField(upload_to = 'images/', null = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "2.5 Team"

class contactDescription(models.Model):
    description = models.CharField(max_length = 150, blank = True, null = True)

    def __str__(self):
        return "Contact Description"

    class Meta:
        verbose_name_plural = "3.1 ContactDescription"
class Contact(models.Model):
    icon = models.CharField(max_length = 200, blank = True, null = True)
    header = models.CharField(max_length = 30, blank = True, null = True)
    content = models.CharField(max_length = 150, blank = True, null = True)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name_plural = "3.2 Contact"

class Footer(models.Model):
    footerDescription = models.TextField(max_length = 500, blank = True, null = True)
    # Use if to check if these links exists on template
    twitterLink = models.URLField(max_length = 200, blank = True, null = True)
    facebookLink = models.URLField(max_length = 200, blank = True, null = True)
    instagramLink = models.URLField(max_length = 200, blank = True, null = True)
    linkedinLink = models.URLField(max_length = 200, blank = True, null = True)
    
    def __str__(self):
        return "Footer"

    class Meta:
        verbose_name_plural = "3.3 Footer"