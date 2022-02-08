from django import views
import django
from django.shortcuts import render
from django.views import View
from .models import profession,username,AboutMe,Skills,Workingjourney,Services,JobExperience,Educations
from django.contrib.auth.models import User

# Create your views here.

class Home(views.View):
    def get(self,request):
        profression= profession.objects.all()
        user=username.objects.all()
        aboutme=AboutMe.objects.all()
        skills=Skills.objects.all()
        workingjourney=Workingjourney.objects.all()
        services=Services.objects.all()
        jobexperience=JobExperience.objects.all()
        educations=Educations.objects.all()

        data={
            'profression':profression,
            'user':user,
            'about':aboutme,
            'skills':skills,
            'workingjourney':workingjourney,
            'services':services,
            'jobexperience':jobexperience,
            'educations':educations

        }
        return render(request,'index.html',data)
