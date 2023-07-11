from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

personal_data = PersonalData.objects.all()
experience = Experience.objects.all()
education = Education.objects.all()
languages = Language.objects.all()
skills = Skill.objects.all()


data = {"first_name": personal_data[0].first_name, "last_name": personal_data[0].last_name, "email": personal_data[0].email, \
            "address": personal_data[0].address, "phone_number": personal_data[0].phone_number, "about_me": personal_data[0].about_me, \
            "profession": personal_data[0].profession, "experience": experience, "education": education, "languages": languages, "skills": skills}

def home(request):
    return render(request, 'index.html', context=data)

def resume(request):
    return render(request, 'resume.html', context=data)

def projects(request):
    return render(request, 'projects.html',context=data)

def contact(request):
    return render(request, 'contact.html', context=data)




# def skills(request):  
#     return render(request, "index.html", context={"soft_skills": ['Շփվող', 'Թիմային աշխատող', 'Խնդիր լուծող', 'Ժամանակի կառավարում'], "hard_skills": ['Հարկային օրենսգիրք', 'Աշխատանքային օրենսգիրք', 'E-invoicing', 'Tax-service', 'HTML', 'CSS', 'Python', 'Django']})


# def languages(request):
#     return render(request, "index.html", context = {"languages": ["հայերեն", "ռուսերեն", "անգլերեն", "գերմաներեն"]})


# def work_experience(request):
#     return render(request, "index.html", context = {"work_experience": [{"period": "2021թ․ present", "title": "Ավագ հաշվապահ", "company_name": "«Լոյալ» հաշվապահական գրասենյակ"}, {"period": "2020-2021", "title": "Թիմի ղեկավար", "company_name": "«Լոյալ» հաշվապահական գրասենյակ"}, {"period": "2018-2020", "title": "Հաշվապահ", "company_name": "«Լոյալ» հաշվապահական գրասենյակ"}, {"period": "2017-2018", "title": "Կրտսեր հաշվապահ", "company_name": "«Լոյալ» հաշվապահական գրասենյակ"}, {"period": "2016-2017", "title": "Պրակտիկանտ", "company_name": "«Ֆին ֊ կոր» հաշվապահական գրասենյակ ՍՊԸ"}]})


# def education(request):
#     return render(request, "index.html", context={"education": [
#         {"period":"2012-2017", "profession": "Բակալավր աուդիտ մասնագիտացմամբ", "place": "ՀՊՏՀ"}, 
#         {"period":"2017", "profession": "Հաշվապահական հաշվառման դասընթաց", "place": "Ֆին ֊ կոր» հաշվապահական գրասենյակ ՍՊԸ"},
#         ]})    


# Create your views here.
