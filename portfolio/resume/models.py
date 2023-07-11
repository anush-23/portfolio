from django.db import models

class PersonalData(models.Model):
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=30)
    address = models.TextField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.TextField(max_length=20)
    about_me = models.TextField(max_length=1000)
    profession = models.TextField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

class Skill(models.Model):
    skill = models.TextField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

class Education(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    university_name = models.TextField(max_length=30)
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
    created_at = models.DateTimeField(auto_now_add=True)

class Language(models.Model):
    language = models.TextField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)





# Create your models here
