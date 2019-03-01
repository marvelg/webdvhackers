from django.contrib import admin
from .models import Slider
from .models import aboutUs
from .models import belowAboutUs
from .models import callToAction
from .models import skillsDescription
from .models import Skill

# Register your models here.
class Static(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Slider)
admin.site.register(aboutUs)
admin.site.register(belowAboutUs)
admin.site.register(callToAction)
admin.site.register(skillsDescription)
admin.site.register(Skill)

