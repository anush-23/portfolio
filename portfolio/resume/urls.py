from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('resume/', resume, name='resume'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
]