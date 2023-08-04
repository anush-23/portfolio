from django.shortcuts import render
from .models import PersonalData, Experience, Education, Language, Skill, Projects

personal_data = PersonalData.objects.get(user__username= "anush")
experience = Experience.objects.all()
education = Education.objects.all()
languages = Language.objects.all()
skills = Skill.objects.all()
projects = Projects.objects.all()


data = {"personal_data": personal_data, "experience": experience, "education": education, "languages": languages,
        "skills": skills, "projects": projects, }


def home(request):
    return render(request, 'index.html', context=data)


def resume(request):
    return render(request, 'resume.html', context=data)


def projects(request):
    return render(request, 'projects.html', context=data)


def contact(request):
    return render(request, 'contact.html', context=data)


def projects(request):
    return render(request, "projects.html", context=data)
