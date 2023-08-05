from django.shortcuts import render
from .models import PersonalData, Experience, Education, Language, Skill, Projects
from .forms import MessageForm

personal_data = PersonalData.objects.get(user__username= "anush")
experience = Experience.objects.all()
education = Education.objects.all()
languages = Language.objects.all()
skills = Skill.objects.all()
projects = Projects.objects.all()
message_form = MessageForm()


data = {"personal_data": personal_data, "experience": experience, "education": education, "languages": languages,
        "skills": skills, "projects": projects, "message_form": message_form}


def home(request):
    return render(request, 'index.html', context=data)


def resume(request):
    return render(request, 'resume.html', context=data)


def projects(request):
    return render(request, 'projects.html', context=data)

def get_in_touch(request):
    return render(request, 'get_in_touch.html', context=data)


def contact(request):
    form = MessageForm(request.POST)
    print(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'contact.html', context=data)


def projects(request):
    return render(request, "projects.html", context=data)