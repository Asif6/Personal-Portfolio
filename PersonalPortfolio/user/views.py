from django import views
from django.shortcuts import render
from django.views import View
from .models import profession,username,AboutMe,Skills,Workingjourney

# Create your views here.

class Home(views.View):
    def get(self,request):
        profression= profession.objects.all()
        user=username.objects.all()
        aboutme=AboutMe.objects.all()
        skills=Skills.objects.all()
        workingjourney=Workingjourney.objects.all()

        data={
            'profression':profression,
            'user':user,
            'about':aboutme,
            'skills':skills,
            'workingjourney':workingjourney
        }
        return render(request,'index.html',data)
