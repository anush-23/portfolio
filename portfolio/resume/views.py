from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

personal_data = PersonalData.objects.all()
experience = Experience.objects.all()
education = Education.objects.all()
languages = Language.objects.all()
skills = Skill.objects.all()
projects = Projects.objects.all()


data = {"first_name": personal_data[0].first_name, "last_name": personal_data[0].last_name, "email": personal_data[0].email, \
            "address": personal_data[0].address, "phone_number": personal_data[0].phone_number, "about_me": personal_data[0].about_me, \
            "profession": personal_data[0].profession, "experience": experience, "education": education, "languages": languages, "skills": skills, "projects": projects,}

def home(request):
    return render(request, 'index.html', context=data)

def resume(request):
    return render(request, 'resume.html', context=data)

def projects(request):
    return render(request, 'projects.html',context=data)

def contact(request):
    return render(request, 'contact.html', context=data)