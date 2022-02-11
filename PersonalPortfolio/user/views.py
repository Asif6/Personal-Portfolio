from django import views
import django
from django.shortcuts import render
from django.views import View
from .models import profession,username,AboutMe,Skills,Workingjourney,Services,JobExperience,Educations,Resent_work,Resent_work_category
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
        resent_work=Resent_work.objects.all()
        resent_work_category=Resent_work_category.objects.all()

        data={
            'profression':profression,
            'user':user,
            'about':aboutme,
            'skills':skills,
            'workingjourney':workingjourney,
            'services':services,
            'jobexperience':jobexperience,
            'educations':educations,
            'resent_work':resent_work,
            'resent_work_category':resent_work_category

        }
        
        
        return render(request,'index.html',data)
