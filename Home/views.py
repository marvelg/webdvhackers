from django.shortcuts import render
from .models import Slider
from .models import aboutUs
from .models import belowAboutUs
from .models import callToAction
from .models import skillsDescription
from .models import Skill

# Create your views here.
def home(request):
    slider = Slider.objects
    aboutus = aboutUs.objects
    belowaboutus = belowAboutUs.objects
    calltoaction = callToAction.objects
    skillsdescription = skillsDescription.objects
    skill = Skill.objects

    return render(request, 'Home/index.html', 
    {"Slider" : slider, "aboutUs":aboutus,
     "belowAboutUs":belowaboutus, "calltoaction":callToAction, "skillsDescription" : skillsdescription,
     "Skill":skill})