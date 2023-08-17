from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class PersonalData(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone_number = models.TextField(max_length=20)
    about_me = models.TextField(max_length=1000)
    profession = models.TextField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    sphere = models.TextField(max_length=30)
    specialization = models.TextField(max_length=30)
    slogan = models.TextField(max_length=100)
    smth_to_say = models.TextField(max_length=200)

class Skill(models.Model):
    skill = models.TextField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

class Education(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    university_name = models.TextField(max_length=100)
    university_city = models.TextField(max_length=20)
    grade = models.TextField(max_length=30)
    discription = models.TextField(max_length=1000, blank = True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, )

class Experience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    position = models.TextField(max_length=30)
    company_name = models.TextField(max_length=100)
    company_city = models.TextField(max_length=20)
    discription = models.TextField(max_length=1000, blank = True, null=True)

class Language(models.Model):
    language = models.TextField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

class Projects(models.Model):
    project_name = models.TextField(max_length=100)
    project_description = models.TextField(max_length=1000)
    project_image = models.ImageField(upload_to='media')
    project_link = models.TextField()
    
class Message(models.Model):
    full_name = models.CharField(max_length=60)
    email = models.EmailField()
    phone_number = models.IntegerField()
    message = models.TextField()