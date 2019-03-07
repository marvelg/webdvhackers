from django.shortcuts import render
from .models import startSlider
from .models import Slider
from .models import aboutUs
from .models import belowAboutUs
from .models import callToAction
from .models import skillsDescription
from .models import Skill
from .models import portfolioCategories
from .models import Project
from .models import teamDescription
from .models import Team
from .models import contactDescription
from .models import Contact
from .models import Footer
# Create your views here.
def home(request):
     startslider = startSlider.objects
     slider = Slider.objects
     aboutus = aboutUs.objects
     belowaboutus = belowAboutUs.objects
     calltoaction = callToAction.objects
     skillsdescription = skillsDescription.objects
     skill = Skill.objects
     portfoliocategories = portfolioCategories.objects
     project = Project.objects
     teamdescription = teamDescription.objects
     team = Team.objects
     contactdescription = contactDescription.objects
     contact = Contact.objects
     footer = Footer.objects

     return render(request, 'Home/index.html', 
    {"startSlider" : startslider, "Slider" : slider, "aboutUs":aboutus,
     "belowAboutUs":belowaboutus, "callToAction":calltoaction, "skillsDescription" : skillsdescription,
     "Skill":skill, "portfolioCategories" : portfoliocategories, "Project" : project , "teamDescription" : teamdescription, 
     "Team" : team, "contactDescription":contactdescription, "Contact" : contact, "Footer" : footer, "Active" : "active"})
     

    