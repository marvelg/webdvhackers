from django.contrib import admin
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
# Register your models here.
class Static(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(startSlider)
admin.site.register(Slider)
admin.site.register(aboutUs)
admin.site.register(belowAboutUs)
admin.site.register(callToAction)
admin.site.register(skillsDescription)
admin.site.register(Skill)
admin.site.register(portfolioCategories)
admin.site.register(Project)
admin.site.register(teamDescription)
admin.site.register(Team)
admin.site.register(contactDescription)
admin.site.register(Contact)
admin.site.register(Footer)



