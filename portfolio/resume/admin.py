from django.contrib import admin
from .models import Skill, Education, Experience, Language, PersonalData

class PersonalDataAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "address", "profession"]

class SkillAdmin(admin.ModelAdmin):
    list_display = ["skill"]

class EducationAdmin(admin.ModelAdmin):
    list_display = ["start_date", "end_date", "university_name", "grade"]

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["start_date", "end_date", "position", "company_name"]

class LanguageAdmin(admin.ModelAdmin):
    list_display = ["language"]

admin.site.register(PersonalData, PersonalDataAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Language, LanguageAdmin)





# Register your models here.
